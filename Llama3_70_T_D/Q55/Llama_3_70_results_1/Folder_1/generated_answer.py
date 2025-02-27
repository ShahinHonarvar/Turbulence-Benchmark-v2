def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i, n + i):
            product = 1
            for k in range(j - i + 1):
                product *= lst[j - k % n]
            if product == -51:
                result.append(lst[j - i:j + 1])
    return result