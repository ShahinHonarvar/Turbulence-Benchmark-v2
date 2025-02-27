def lists_with_product_equal_n(circular_list):
    n = 29
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        j = i
        while len(sublist) < len(circular_list):
            sublist.append(circular_list[j])
            product *= circular_list[j]
            if product == n:
                result.append(sublist.copy())
            j = (j + 1) % len(circular_list)
            if j == i:
                break
    return result