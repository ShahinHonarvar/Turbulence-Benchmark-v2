def lists_with_product_equal_n(circular_list):
    n = 51
    result = []
    length = len(circular_list)
    extended_list = circular_list + circular_list[:-1]
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= extended_list[end]
            if product == n:
                result.append(extended_list[start:end + 1])
            if product == 0 or product > n:
                break
    return result