def lists_with_product_equal_n(circular_list):
    n = -56
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
            if product == 0 or product == n or product == -n:
                break
        if product == n:
            for j in range(1, len(sublist)):
                sublist.pop(0)
                product //= circular_list[start]
                if product == n:
                    result.append(sublist.copy())
    return result