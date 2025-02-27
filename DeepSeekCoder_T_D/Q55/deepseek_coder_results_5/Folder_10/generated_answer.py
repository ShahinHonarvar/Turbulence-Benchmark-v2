def lists_with_product_equal_n(circular_list):
    n = -93
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
            if product != 1 and (product % n == 0 or product == n):
                continue
            else:
                break
        if product == n:
            for j in range(1, len(sublist)):
                result.append(sublist[j:] + circular_list[:j])
    return result