def lists_with_product_equal_n(num_list):
    n = len(num_list)
    result = []
    for i in range(n):
        product = num_list[i]
        for j in range(i + 1, n + i):
            product *= num_list[j % n]
            if product == -15:
                result.append(num_list[i:j % n + 1])
    return result