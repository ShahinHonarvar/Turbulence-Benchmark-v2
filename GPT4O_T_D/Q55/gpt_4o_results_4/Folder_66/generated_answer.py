def lists_with_product_equal_n(circular_list):
    n = 78
    length = len(circular_list)
    result = []
    for i in range(length):
        product = 1
        current_sublist = []
        for j in range(length):
            index = (i + j) % length
            product *= circular_list[index]
            current_sublist.append(circular_list[index])
            if product == n:
                result.append(current_sublist.copy())
            if product == 0 or product > n:
                break
    return result