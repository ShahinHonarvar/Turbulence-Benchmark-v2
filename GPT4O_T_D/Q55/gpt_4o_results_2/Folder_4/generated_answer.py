def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        sublist = []
        for i in range(length):
            idx = (start + i) % length
            sublist.append(circular_list[idx])
            product *= circular_list[idx]
            if product == 91:
                result.append(sublist[:])
            if product == 0 or product > 91:
                break
    return result