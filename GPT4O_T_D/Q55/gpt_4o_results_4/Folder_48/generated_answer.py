def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= circular_list[index]
            if product == 990 and length <= n:
                end_index = (start + length) % n
                if end_index > start:
                    sublist = circular_list[start:end_index]
                else:
                    sublist = circular_list[start:] + circular_list[:end_index]
                result.append(sublist)
            if product == 0:
                break
    return result