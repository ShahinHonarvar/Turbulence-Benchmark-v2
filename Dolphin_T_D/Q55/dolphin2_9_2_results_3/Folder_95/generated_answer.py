def lists_with_product_equal_n(lst):
    n = len(lst)
    product = 1
    result = []
    for start in range(n):
        product = 1
        for end in range(start, n):
            product *= lst[end]
            if product == 28:
                result.append(lst[start:end + 1])
    return result