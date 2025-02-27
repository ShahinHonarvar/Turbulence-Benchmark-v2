def lists_with_product_equal_n(circular_list):
    n = 53
    result = []
    circular_list *= 2
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == n:
                result.append(circular_list[i:j + 1])
    return result