def lists_with_product_equal_n(data):
    result = []
    for i in range(len(data)):
        for j in range(i, len(data)):
            sublist = data[i:j + 1]
            if 0 in sublist:
                result.append(sublist)
    for i in range(len(data)):
        for j in range(i):
            sublist = data[i:] + data[:j]
            if 0 in sublist:
                result.append(sublist)
    return result