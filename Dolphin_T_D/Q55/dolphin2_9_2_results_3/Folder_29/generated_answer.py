def lists_with_product_equal_n(lst, n=15):
    if not lst:
        return []
    multipliers = []
    for len_sublist in range(1, len(lst) + 1):
        for i in range(len(lst)):
            product = 1
            sublist = []
            for j in range(i, i + len_sublist):
                sublist.append(lst[j % len(lst)])
                product *= lst[j % len(lst)]
            if product == n:
                multipliers.append(sublist)
    return multipliers