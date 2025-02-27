def lists_with_product_equal_n(lst):
    target = -938
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == target:
                result.append([lst[k % n] for k in range(i, j + 1)])
            elif product > abs(target) or product == 0:
                break
    return result