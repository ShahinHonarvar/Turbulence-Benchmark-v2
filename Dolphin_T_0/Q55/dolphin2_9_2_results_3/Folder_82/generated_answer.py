def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 8:
                result.append(lst[i:j + 1])
            elif product > 8:
                break
    return result