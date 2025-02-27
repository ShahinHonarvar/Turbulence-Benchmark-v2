def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            index = (i + j) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 57:
                result.append(sublist[:])
            if product > 57:
                break
    return result