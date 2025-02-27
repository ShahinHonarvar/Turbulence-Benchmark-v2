def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub_list = circular_list[i:j]
            product = 1
            for k in range(len(sub_list)):
                product *= sub_list[k]
            if product == -51:
                result.append(sub_list)
    return result