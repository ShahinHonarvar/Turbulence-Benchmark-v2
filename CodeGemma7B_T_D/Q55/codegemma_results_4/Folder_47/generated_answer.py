def lists_with_product_equal_n(list):
    n = -94
    output = []
    for i in range(len(list)):
        for j in range(i, len(list)):
            product = 1
            for k in range(i, j + 1):
                product *= list[k]
            if product == n:
                output.append(list[i:j + 1])
    return output