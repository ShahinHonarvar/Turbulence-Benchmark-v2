def lists_with_product_equal_n(circular_list):
    n = -115
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        for end in range(length):
            product *= circular_list[(start + end) % length]
            if abs(product) > abs(n):
                break
            if product == n:
                end_idx = (start + end) % length
                if start <= end_idx:
                    result.append(circular_list[start:end_idx + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:end_idx + 1])
                break
    return result