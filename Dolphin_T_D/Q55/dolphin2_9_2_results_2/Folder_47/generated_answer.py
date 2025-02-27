def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    product = -94
    if n < 1:
        return sublists
    if n == 1:
        if lst[0] == product:
            sublists.append([lst[0]])
    for i in range(n):
        product_so_far = 1
        for j in range(i, n):
            product_so_far *= lst[j]
            if j - i + 2 < n:
                product_so_far *= lst[(j - i + 2) % n]
            if product_so_far == product:
                sublist = []
                for k in range(i, j + 1):
                    sublist.append(lst[k])
                sublists.append(sublist)
    return sublists