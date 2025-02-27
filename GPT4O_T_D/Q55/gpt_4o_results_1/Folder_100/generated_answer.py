def lists_with_product_equal_n(circular_list):
    n = 48
    length = len(circular_list)
    result = []
    for start in range(length):
        product = 1
        sublist = []
        for i in range(length):
            index = (start + i) % length
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist.copy())
            if product == 0 or product > n:
                break
    return result