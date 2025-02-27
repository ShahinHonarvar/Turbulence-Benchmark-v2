def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for size in range(n):
            index = (start + size) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == -23:
                result.append(sublist[:])
    return result