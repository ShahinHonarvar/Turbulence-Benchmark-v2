def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    for i in range(n):
        cur_product = 1
        for j in range(n):
            cur_product *= lst[(i + j) % n]
            if cur_product == 46:
                result.append(lst[(i + j - n + 1) % n:(i + j + 1) % n])
    return result