def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    target_product = 51
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == target_product:
                result.append([lst[(i + k) % n] for k in range(j + 1)])
            elif product > target_product:
                break
    return result