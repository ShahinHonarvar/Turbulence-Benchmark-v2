def lists_with_product_equal_n(lst):
    n = len(lst)
    target_product = -115
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == target_product:
                result.append(lst[i:i + j + 1] if i + j + 1 <= n else lst[i:] + lst[:j - n + i + 1])
            elif product > abs(target_product):
                break
    return result