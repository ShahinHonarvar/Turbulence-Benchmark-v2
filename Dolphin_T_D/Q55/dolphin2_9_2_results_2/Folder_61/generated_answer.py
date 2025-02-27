def lists_with_product_equal_n(input_list):
    n = len(input_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= input_list[j % n]
            if product == -10:
                result.append(input_list[i:j % n + 1])
    return result