def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == 53:
                result.append(lst[i:i + j + 1])
            elif product > 53:
                break
    return result