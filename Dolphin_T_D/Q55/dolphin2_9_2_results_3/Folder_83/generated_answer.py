def lists_with_product_equal_n(lst, n=-57):
    l = len(lst)
    sublists = []
    for size in range(1, l + 1):
        for i in range(l):
            prod = 1
            sub = []
            for j in range(i, i + size):
                prod *= lst[j % l]
                sub.append(lst[j % l])
            if prod == n:
                sublists.append(sub)
    return sublists