def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product > 57:
                break
            if product == 57:
                sublist = []
                for k in range(i, j):
                    sublist.append(lst[k % n])
                sublists.append(sublist)
    return sublists