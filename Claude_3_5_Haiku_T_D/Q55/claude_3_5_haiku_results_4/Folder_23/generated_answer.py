def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            current_index = (start + i) % n
            product *= circular_list[current_index]
            sublist.append(circular_list[current_index])
            if product == -95:
                result.append(list(sublist))
            if product > -95:
                break
    return result