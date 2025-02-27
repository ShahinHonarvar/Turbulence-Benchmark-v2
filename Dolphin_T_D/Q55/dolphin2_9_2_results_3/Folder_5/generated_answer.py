def lists_with_product_equal_n(lst, n=-33):
    if not lst:
        return []
    lst = lst + lst[:-1]
    i, j = (0, 1)
    result = []
    while j < len(lst):
        product = 1
        for k in range(i, j):
            product *= lst[k]
        if product == n:
            result.append(lst[i:j])
            i = j = j + 1
        elif product < n:
            j += 1
        else:
            i += 1
            if i == j:
                j += 1
    return result