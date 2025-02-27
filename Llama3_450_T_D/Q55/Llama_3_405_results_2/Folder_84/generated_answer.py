def lists_with_product_equal_n(lst):
    n = len(lst)
    target = -906
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == target:
                result.append([lst[(i + k) % n] for k in range(j + 1)])
            elif product > abs(target):
                break
    return result