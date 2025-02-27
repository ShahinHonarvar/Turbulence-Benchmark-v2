def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n - 1):
            index = (i + j) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == -65:
                result.append(sublist.copy())
            if abs(product) > abs(-65):
                break
    return result