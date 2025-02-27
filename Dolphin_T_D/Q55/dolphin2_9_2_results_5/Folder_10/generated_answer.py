def lists_with_product_equal_n(lst):
    if not lst:
        return []
    sublists = []
    n = len(lst)
    for length in range(1, n + 1):
        for i in range(0, n):
            product = 1
            sublist = []
            for j in range(i, i + length):
                sublist.append(lst[j % n])
                product *= lst[j % n]
                if product == -93:
                    sublists.append(sublist)
    return sublists