def lists_with_product_equal_n(circular_list):
    n = 29
    result = []
    if not circular_list:
        return result
    length = len(circular_list)
    circular_list += circular_list
    for start in range(length):
        product = 1
        for end in range(start, start + length):
            product *= circular_list[end]
            if product == n:
                result.append(circular_list[start:end + 1])
            if product != 0 and n % product != 0:
                break
    return result