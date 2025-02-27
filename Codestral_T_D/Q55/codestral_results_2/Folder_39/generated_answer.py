def lists_with_product_equal_n(circular_list):
    n = -46
    result = []
    size = len(circular_list)
    circular_list += circular_list
    for i in range(size):
        product = 1
        sublist = []
        for j in range(i, i + size):
            product *= circular_list[j]
            sublist.append(circular_list[j])
            if product == n:
                result.append(sublist)
            if abs(product) > abs(n):
                break
    return result