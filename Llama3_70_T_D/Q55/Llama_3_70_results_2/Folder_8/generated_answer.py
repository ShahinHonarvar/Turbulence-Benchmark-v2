def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            k = (i + j) % len(lst)
            product *= lst[k]
            if product == -41:
                result.append(lst[k - j:k] if k >= j else lst[k:] + lst[:j])
    return result