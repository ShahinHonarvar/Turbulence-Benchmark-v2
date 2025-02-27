def lists_with_product_equal_n(lst):
    result = []
    product_n = -26
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == product_n:
                result.append(lst[i:j + 1])
            elif product > product_n:
                break
    return result