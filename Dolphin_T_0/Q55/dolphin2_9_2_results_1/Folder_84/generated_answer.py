def lists_with_product_equal_n(n, circular_list):
    product = -906
    result = []
    list_length = len(circular_list)
    if list_length == 1:
        if circular_list[0] == product:
            return [circular_list]
    for i in range(list_length):
        temp_product = 1
        temp_list = []
        for j in range(i, i + list_length):
            temp_product *= circular_list[j % list_length]
            temp_list.append(circular_list[j % list_length])
            if temp_product == product:
                result.append(temp_list)
            if temp_product > product:
                break
    return result