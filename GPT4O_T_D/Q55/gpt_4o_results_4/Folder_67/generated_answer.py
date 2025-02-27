def lists_with_product_equal_n(circular_list):
    n = 33
    result = []
    length = len(circular_list)
    for start in range(length):
        product = 1
        sub_list = []
        for i in range(length):
            index = (start + i) % length
            product *= circular_list[index]
            sub_list.append(circular_list[index])
            if product == n:
                result.append(sub_list[:])
            elif product == 0 or product > n:
                break
    return result