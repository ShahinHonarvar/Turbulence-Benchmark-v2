def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    target_product = 415
    n = len(circular_list)
    results = []
    for start in range(n):
        product = 1
        for length in range(n):
            index = (start + length) % n
            product *= circular_list[index]
            if product == target_product:
                end = (start + length + 1) % n
                if end > start:
                    results.append(circular_list[start:end])
                else:
                    results.append(circular_list[start:] + circular_list[:end])
            if product == 0 or product > target_product:
                break
    return results