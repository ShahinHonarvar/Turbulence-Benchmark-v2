def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        temp = []
        for j in range(i, n):
            product *= circular_list[j]
            temp.append(circular_list[j])
            if product == 6:
                result.append(temp.copy())
    return result