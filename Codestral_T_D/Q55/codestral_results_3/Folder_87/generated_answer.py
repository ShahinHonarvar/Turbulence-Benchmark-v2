def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    lst = lst + lst
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= lst[j]
            sublist.append(lst[j])
            if product == 27:
                sublists.append(sublist)
            if product > 27:
                break
    return sublists