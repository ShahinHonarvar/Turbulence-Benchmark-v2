def lists_with_product_equal_n(circular_list):
    n = 537
    result = []
    for i in range(len(circular_list)):
        product = 1
        sublist = []
        j = i
        while True:
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == n:
                result.append(sublist.copy())
            if product >= n or j == len(circular_list) - 1:
                break
            j = (j + 1) % len(circular_list)
    return result