def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    result = []
    target = 15
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == target:
                result.append(lst[i:j + 1])
            elif product > target:
                break
    return result