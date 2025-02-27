def lists_with_product_equal_n(data):
    result = []
    for i in range(len(data)):
        for j in range(i, len(data)):
            if -23 == reduce(lambda x, y: x * y, data[i:j + 1], 1):
                result.append(data[i:j + 1])
    return result