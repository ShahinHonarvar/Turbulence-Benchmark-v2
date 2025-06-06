def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == -6:
                result.append(sublist.copy())
            if product == 0 or product == -6:
                product = 1
                sublist = []
        if product == -6:
            result.append(sublist)
    return result