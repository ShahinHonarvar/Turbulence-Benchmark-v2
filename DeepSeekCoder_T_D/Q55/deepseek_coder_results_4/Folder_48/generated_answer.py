def lists_with_product_equal_n(circular_list):
    n = 990
    result = []
    list_size = len(circular_list)
    for start in range(list_size):
        product = 1
        sublist = []
        for i in range(list_size):
            index = (start + i) % list_size
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist.copy())
            if product >= n:
                break
    return result