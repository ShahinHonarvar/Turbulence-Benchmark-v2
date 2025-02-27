def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            index = (i + j) % n
            product *= circular_list[index]
            if product == 99:
                sublist_length = j + 1
                sublist = [circular_list[(i + k) % n] for k in range(sublist_length)]
                result.append(sublist)
            if product > 99:
                break
    return result