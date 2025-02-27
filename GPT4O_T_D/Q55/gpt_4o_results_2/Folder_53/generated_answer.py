def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -87
    results = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            if product == target_product:
                end_index = i + j + 1 if i + j + 1 <= n else i + j + 1 - n
                if end_index > i:
                    results.append(circular_list[i:end_index])
                else:
                    results.append(circular_list[i:] + circular_list[:end_index])
    return results