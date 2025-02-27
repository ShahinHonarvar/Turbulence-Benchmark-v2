import math

def lists_with_product_equal_n(lst, n=-22):
    result = []
    for i in range(len(lst)):
        if lst[i] == n:
            result.append([lst[i]])
        product = n
        for j in range(i + 1, len(lst) + i):
            product /= lst[j - 1]
            if product == 1:
                tmp = lst[j - 1:i]
                tmp.reverse()
                result.append(tmp)
            if j == len(lst):
                break
    return result