def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 0:
                result.append(sublist.copy())
                sublist = []
                product = 1
        if sublist and product == 0:
            result.append(sublist)
    return result