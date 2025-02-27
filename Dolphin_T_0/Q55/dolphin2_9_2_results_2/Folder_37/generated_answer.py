def lists_with_product_equal_n(l, n=-76):
    if not l:
        return []
    lst = []
    for i in range(len(l)):
        product = 1
        for sublist_size in range(1, len(l) + 1):
            for j in range(i, i + sublist_size):
                product *= l[j % len(l)]
            if product == n:
                lst.append(l[j % len(l):i + sublist_size])
    return lst