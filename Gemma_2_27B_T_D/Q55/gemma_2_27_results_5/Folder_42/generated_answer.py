def lists_with_product_equal_n(data):
    result = []
    for i in range(len(data)):
        for j in range(i, len(data)):
            sublist = data[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == 25:
                result.append(sublist)
    return result