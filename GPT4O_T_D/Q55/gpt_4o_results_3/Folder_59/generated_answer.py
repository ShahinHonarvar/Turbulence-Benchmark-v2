def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            if product == -3:
                result.append(circular_list[i:i + j + 1] if i + j < n else circular_list[i:] + circular_list[:index + 1])
    return result