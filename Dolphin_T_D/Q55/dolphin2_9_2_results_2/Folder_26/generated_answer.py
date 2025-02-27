def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        cur_product = 1
        cur_list = []
        for j in range(i, i + len(circular_list)):
            if j % len(circular_list) == i:
                break
            cur_product *= circular_list[j % len(circular_list)]
            cur_list.append(circular_list[j % len(circular_list)])
            if cur_product == 93 and len(cur_list) <= len(circular_list):
                result.append(cur_list)
    return result