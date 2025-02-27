def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n - 1, n + 1):
        for j in range(n):
            current_product = 1
            for k in range(i):
                current_product *= lst[(j + k) % n]
            if current_product == 247:
                result.append([lst[(j + m) % n] for m in range(i)])
    return result