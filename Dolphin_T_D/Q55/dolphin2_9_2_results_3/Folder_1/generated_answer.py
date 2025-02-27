from itertools import combinations

def lists_with_product_equal_n(lst, n=-51):
    length = len(lst)
    if length == 0:
        return []
    result = []
    for i in range(length):
        for j in range(i + 1, length + 1):
            if i == j:
                if lst[i] == n:
                    result.append([lst[i]])
            elif i == 0 and j == length:
                list_tmp = [lst[-1]] + lst[0:length - 1]
                if n == 1 or (n != -1 and n not in list_tmp):
                    continue
                for k in range(length - 1):
                    comb = list_tmp[k:k + length - 1]
                    product = 1
                    for m in comb:
                        product *= m
                    if product == n:
                        result.append(comb)
            else:
                list_tmp = lst[i:j]
                if n == 1 or (n != -1 and n not in list_tmp):
                    continue
                for k in range(j - i):
                    comb = list_tmp[k:k + length - 1]
                    product = 1
                    for m in comb:
                        product *= m
                    if product == n:
                        result.append(comb)
    return result