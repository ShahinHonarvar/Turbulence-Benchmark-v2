def lists_with_product_equal_n(lst):
    n = len(lst)
    target_product = -95
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == target_product:
                result.append([lst[k % n] for k in range(i, j + 1)])
            elif product == 0:
                break
    return result