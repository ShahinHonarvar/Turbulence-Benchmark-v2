def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        if lst[i] == 7 or lst[i] == -7:
            sublists.append([lst[i]])
    for size in range(2, n + 1):
        for i in range(n):
            prod = 1
            for j in range(i, i + size):
                prod *= lst[j % n]
            if prod == 49:
                sublists.append(lst[i:i + size])
    return sublists