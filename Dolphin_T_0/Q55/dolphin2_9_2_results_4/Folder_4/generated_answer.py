def lists_with_product_equal_n(lst):
    n = len(lst)
    lst = lst + lst
    sublists = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, n + i):
            product *= lst[j]
            sublist.append(lst[j])
            if product == 91:
                sublists.append(sublist)
    return sublists