def lists_with_product_equal_n(data):
    n = len(data)
    result = []
    for i in range(n):
        for j in range(i, n):
            product = 1
            sublist = data[i:j + 1]
            for num in sublist:
                product *= num
            if product == -30:
                result.append(sublist)
    return result