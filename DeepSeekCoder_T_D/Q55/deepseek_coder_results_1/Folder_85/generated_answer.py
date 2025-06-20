def lists_with_product_equal_n(circular_list):
    n = -97
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
            if product == 0 or product == n:
                product = 1
                sublist = []
            if product > n and circular_list[index] != 0:
                break
    return result