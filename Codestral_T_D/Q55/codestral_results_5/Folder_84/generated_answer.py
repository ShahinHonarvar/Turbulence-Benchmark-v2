import itertools

def lists_with_product_equal_n(lst):
    lst = lst + lst
    n = len(lst) // 2
    sublists = []
    for i in range(n):
        for j in range(i + 1, n + i + 1):
            sublist = lst[i:j]
            product = 1
            for num in sublist:
                product *= num
            if product == -906:
                sublists.append(sublist)
    return sublists