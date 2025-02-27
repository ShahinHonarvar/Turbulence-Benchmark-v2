def lists_with_product_equal_n(circular_list):
    n = 5
    result = []
    list_len = len(circular_list)
    for start in range(list_len):
        product = 1
        sub_list = []
        for i in range(list_len):
            index = (start + i) % list_len
            product *= circular_list[index]
            sub_list.append(circular_list[index])
            if product == n:
                result.append(sub_list[:])
            elif product == 0 or product > n:
                break
    return result