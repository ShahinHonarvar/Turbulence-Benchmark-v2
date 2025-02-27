def lists_with_product_equal_n(circular_list):
    n = -94
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        sublist = []
        for offset in range(length):
            index = (start + offset) % length
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == n:
                result.append(sublist[:])
            if len(sublist) >= length:
                break
    return result