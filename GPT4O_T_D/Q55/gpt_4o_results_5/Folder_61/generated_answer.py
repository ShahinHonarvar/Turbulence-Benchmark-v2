def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            if product == -10:
                end_index = index + 1 if index >= i else index + 1 + n
                result.append(circular_list[i:end_index % n] if end_index % n else circular_list[i:] + circular_list[:end_index % n])
    return result