def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    circular_list = circular_list * 2
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= circular_list[end]
            if product == 8:
                result.append(circular_list[start:end + 1])
            if product == 0 or product > 8:
                break
    return result