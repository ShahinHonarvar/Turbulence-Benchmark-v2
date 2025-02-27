def lists_with_product_equal_n(lst):
    n = -61
    size = len(lst)
    result = []
    for i in range(size):
        if lst[i] == 0:
            continue
        prod = lst[i]
        for j in range(i + 1, i + size):
            prod *= lst[j % size]
            if prod == n:
                result.append(lst[i:j % size + 1])
    return result