def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == -17:
                result.append([lst[(i + k) % n] for k in range(j - i + 1)])
            elif product == 0:
                break
    return result