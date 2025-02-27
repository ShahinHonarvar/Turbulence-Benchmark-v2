def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for length in range(n):
            index = (start + length) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == 990:
                result.append(sublist[:])
            if product > 990:
                break
    return result