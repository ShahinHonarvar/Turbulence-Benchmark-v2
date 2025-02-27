def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    target_product = -76
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            if product == target_product:
                start = i
                end = index + 1
                if end <= n:
                    result.append(circular_list[start:end])
                else:
                    result.append(circular_list[start:] + circular_list[:end % n])
    return result