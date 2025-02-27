def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(1, length + 1):
            product *= lst[(i + j - 1) % length]
            if product > 29:
                break
            if product == 29:
                result.append(lst[(i + j - 1) % length:j + i])
    return result