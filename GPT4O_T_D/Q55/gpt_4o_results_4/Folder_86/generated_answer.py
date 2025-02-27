def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    target_product = -779
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            idx = (start + length - 1) % n
            product *= circular_list[idx]
            if product == target_product:
                end = (start + length - 1) % n
                if end >= start:
                    result.append(circular_list[start:end + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:end + 1])
    return result