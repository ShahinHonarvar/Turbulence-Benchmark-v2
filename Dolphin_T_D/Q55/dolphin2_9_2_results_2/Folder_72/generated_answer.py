def lists_with_product_equal_n(num_list, n):
    result = []
    length = len(num_list)
    for i in range(length):
        for j in range(i, length):
            product = 1
            for k in range(i, j + 1):
                product *= num_list[k]
            if product == n:
                result.append(num_list[i:j + 1])
    return result