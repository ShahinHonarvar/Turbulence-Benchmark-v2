def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == -81:
                result.append(lst[i:j % n + 1] if j < i + n - 1 else lst[i:] + lst[:j % n + 1])
    return result