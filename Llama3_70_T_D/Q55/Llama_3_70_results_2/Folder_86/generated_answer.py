def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            k = (i + j) % n
            product *= lst[k]
            if product == -779:
                result.append(lst[k - j:k] or [lst[k]] + lst[:k - j])
    return result