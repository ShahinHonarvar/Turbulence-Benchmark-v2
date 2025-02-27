from itertools import combinations

def lists_with_product_equal_n(lst):
    n = -3
    lst += lst
    res = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = lst[i:j]
            if len(sublist) <= len(lst) // 2:
                product = 1
                for num in sublist:
                    product *= num
                if product == n:
                    res.append(sublist)
    return res