def lists_with_product_equal_n(lst):
    n = 15
    result = []
    for i in range(len(lst)):
        if lst[i] == n:
            result.append([lst[i]])
        prod = lst[i]
        for j in range(i + 1, len(lst) + i):
            if prod * lst[j % len(lst)] == n:
                result.append(lst[i:j % len(lst) + 1])
            prod *= lst[j % len(lst)]
    return result