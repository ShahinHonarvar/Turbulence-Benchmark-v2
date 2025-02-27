def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -56
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target_product:
                result.append(sublist.copy())
            if product == 0 or product == target_product:
                product = 1
                sublist = []
        if product == target_product:
            result.append(sublist)
    return result