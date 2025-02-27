def lists_with_product_equal_n(circular_list):
    result = []
    n = 714
    length = len(circular_list)
    for start in range(length):
        product = 1
        sublist = []
        for offset in range(length):
            index = (start + offset) % length
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist.copy())
            if product == 0 or product > n:
                break
    return result