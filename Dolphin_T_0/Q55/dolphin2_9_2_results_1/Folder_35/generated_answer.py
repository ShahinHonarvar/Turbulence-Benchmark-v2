def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n + 1):
            product = 1
            sublist = []
            for k in range(i, j):
                sublist.append(lst[k % n])
                product *= lst[k % n]
            if product == 83:
                sublists.append(sublist)
                sublists.append(sublist[::-1])
    return sublists