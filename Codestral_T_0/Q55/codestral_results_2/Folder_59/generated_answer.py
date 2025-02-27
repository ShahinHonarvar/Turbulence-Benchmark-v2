def lists_with_product_equal_n(lst):
    n = -3
    result = []
    for i in range(len(lst)):
        if lst[i] == n:
            result.append([lst[i]])
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
    return result