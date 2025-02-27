def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == -1:
                result.append(sublist[:])
    return result