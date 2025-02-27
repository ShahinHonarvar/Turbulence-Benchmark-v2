def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    result = []
    n = 99
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == n:
                result.append(lst[i:i + j + 1])
            elif product > n:
                break
    return result