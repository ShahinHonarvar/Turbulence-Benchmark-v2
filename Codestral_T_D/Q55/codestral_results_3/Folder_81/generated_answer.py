def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= circular_list[j % n]
            sublist.append(circular_list[j % n])
            if product == -8:
                result.append(sublist)
            elif product != 0 and abs(product) < 8:
                break
    return result