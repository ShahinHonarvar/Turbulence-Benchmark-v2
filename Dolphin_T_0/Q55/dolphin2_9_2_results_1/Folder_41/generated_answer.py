def lists_with_product_equal_n(lst):
    n = len(lst)
    if n == 0:
        return []
    lst = lst + lst[:2]
    sublists = []
    product = 1
    for i in range(n + 2):
        if i > 0:
            product *= lst[i]
        if product == -20:
            sublist = lst[i - n:i]
            if len(sublist) > 1 and (not sublist in sublists):
                sublists.append(sublist)
    return sublists