def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        product = 1
        sublist = []
        j = i
        while True:
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == 85:
                result.append(sublist.copy())
            j = (j + 1) % n
            if j == i:
                break
    return result