def lists_with_product_equal_n(data):
    result = []
    for i in range(len(data)):
        for j in range(i, len(data)):
            sublist = data[i:j + 1] + data[:i] if j >= i else data[i:j + 1]
            if len(sublist) > 0 and reduce(lambda x, y: x * y, sublist) == -54:
                result.append(sublist)
    return result