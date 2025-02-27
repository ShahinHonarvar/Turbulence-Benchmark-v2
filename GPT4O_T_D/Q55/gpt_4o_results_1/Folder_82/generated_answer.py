def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        for size in range(1, n + 1):
            idx = (i + size - 1) % n
            product *= circular_list[idx]
            if product == 8:
                if size <= n:
                    end_index = (i + size - 1) % n
                    if end_index >= i:
                        result.append(circular_list[i:end_index + 1])
                    else:
                        result.append(circular_list[i:] + circular_list[:end_index + 1])
            elif product == 0:
                break
    return result