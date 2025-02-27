def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        sublist = []
        for offset in range(size):
            index = (start + offset) % size
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 93:
                result.append(sublist[:])
                break
            if product > 93 or product == 0:
                break
    return result