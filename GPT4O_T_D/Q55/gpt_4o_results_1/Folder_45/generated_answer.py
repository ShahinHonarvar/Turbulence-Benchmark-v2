def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= circular_list[index]
            if product == -5:
                if start <= index:
                    result.append(circular_list[start:index + 1])
                else:
                    result.append(circular_list[start:] + circular_list[:index + 1])
    return result