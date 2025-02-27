def lists_with_product_equal_n(list_input):
    result = []
    size = len(list_input)
    for i in range(size):
        z = 1
        for j in range(i, i + size):
            z *= list_input[j % size]
            if z > 76:
                break
            if z == 76:
                result.append(list(list_input[i % size:j % size + 1]))
    return result