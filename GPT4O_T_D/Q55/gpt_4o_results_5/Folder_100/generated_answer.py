def lists_with_product_equal_n(circular_list):
    n = 48
    size = len(circular_list)
    result = []
    for start in range(size):
        product = 1
        temp_list = []
        for offset in range(size):
            index = (start + offset) % size
            product *= circular_list[index]
            temp_list.append(circular_list[index])
            if product == n:
                result.append(temp_list[:])
            if product == 0 or product > n:
                break
    return result