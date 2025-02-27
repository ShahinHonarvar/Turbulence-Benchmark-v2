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
            if product == 0 or product == n or abs(product) > abs(n):
                break
        if product == n:
            for i in range(1, list_size):
                index = (start + i) % list_size
                sublist.pop(0)
                sublist.append(circular_list[index])
                if product == n:
                    result.append(sublist.copy())
                else:
                    break
    return result