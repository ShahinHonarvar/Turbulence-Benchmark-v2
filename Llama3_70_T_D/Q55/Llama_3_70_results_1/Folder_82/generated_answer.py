def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == 8:
                result.append(lst[i:(i + j + 1) % n] if (i + j + 1) % n > i else lst[i:] + lst[:(i + j + 1) % n])
            elif product > 8:
                break
    return result