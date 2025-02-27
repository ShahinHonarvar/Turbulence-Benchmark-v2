def lists_with_product_equal_n(lst):
    result = []
    length = len(lst)
    for i in range(length):
        product = 1
        for j in range(length):
            product *= lst[(i + j) % length]
            if product == 49:
                result.append(lst[(i + j) % length - j:i + j + 1])
            if product > 49:
                break
    return result