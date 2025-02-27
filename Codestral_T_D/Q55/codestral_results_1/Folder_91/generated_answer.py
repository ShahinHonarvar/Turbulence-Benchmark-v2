from itertools import combinations

def lists_with_product_equal_n(lst):
    n = 2
    len_lst = len(lst)
    lst += lst
    result = []
    for i in range(len_lst):
        for j in range(i + 1, i + len_lst):
            product = 1
            for k in range(i, j):
                product *= lst[k]
                if product > n:
                    break
                if product == n:
                    result.append(lst[i:j])
    return result