def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    if n == 0:
        return []
    product = 1
    for i in range(n):
        product *= lst[i]
    if product == 42:
        sublists.append(lst)
    for i in range(n):
        product_left = 1
        if i > 0:
            product_left = lst[0]
        for j in range(i + 1, n):
            product_left *= lst[j - i]
            product_right = 1
            for k in range(j, n):
                k = k % n
                product_right *= lst[k]
                if product_left * product_right == 42 and j - i > 0:
                    sublist = []
                    for m in range(i, j):
                        sublist.append(lst[m % n])
                    sublists.append(sublist)
    return sublists