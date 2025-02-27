def lists_with_product_equal_n(lst):
    target = -33
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == target:
                result.append([lst[k % n] for k in range(i, j + 1)])
            elif product > target or j - i + 1 == n:
                break
    return result