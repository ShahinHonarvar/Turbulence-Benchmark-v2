def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == -9:
                result.append(lst[i:i + j + 1])
            if product < 0:
                break
    return result