def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for i in range(n):
            idx = (start + i) % n
            product *= circular_list[idx]
            if product == 85:
                end = (start + i + 1) % n
                if start < end:
                    result.append(circular_list[start:end])
                else:
                    result.append(circular_list[start:] + circular_list[:end])
            if product == 0:
                break
    return result