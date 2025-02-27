def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(n):
            index = (start + length) % n
            product *= circular_list[index]
            if product == 46:
                if length + 1 <= n:
                    end = index + 1 if index + 1 <= n else (index + 1) % n
                    if start < end:
                        result.append(circular_list[start:end])
                    else:
                        result.append(circular_list[start:] + circular_list[:end])
    return result