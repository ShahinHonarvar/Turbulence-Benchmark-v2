def lists_with_product_equal_n(lst):
    target_product = -94
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == target_product:
                result.append(lst[i:j + 1])
            elif product > abs(target_product) and target_product < 0 or (product < abs(target_product) and target_product > 0):
                break
    return result