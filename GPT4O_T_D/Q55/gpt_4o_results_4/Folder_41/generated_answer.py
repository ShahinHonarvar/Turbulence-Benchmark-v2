def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    circular_list = circular_list * 2
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end]
            if product == -20:
                result.append(circular_list[start:end + 1])
            if circular_list[end] == 0:
                break
    return result