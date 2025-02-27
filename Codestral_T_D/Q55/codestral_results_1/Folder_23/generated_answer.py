def lists_with_product_equal_n(lst):
    n = -95
    result = []
    for i in range(len(lst)):
        if lst[i] == n:
            result.append([lst[i]])
        product = lst[i]
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
    return result