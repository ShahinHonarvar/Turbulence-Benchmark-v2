def lists_with_product_equal_n(data):
    if len(data) == 0:
        return []
    result = []
    for i in range(len(data)):
        product = 1
        for j in range(i, len(data)):
            product *= data[j]
            if product == 6:
                result.append(data[i:j + 1])
    return result