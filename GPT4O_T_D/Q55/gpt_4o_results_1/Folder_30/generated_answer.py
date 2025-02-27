def lists_with_product_equal_n(circular_list):
    n = 99
    result = []
    l = len(circular_list)
    for start in range(l):
        product = 1
        sublist = []
        for offset in range(l):
            index = (start + offset) % l
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == n:
                result.append(sublist.copy())
            if product == 0 or product > n:
                break
    return result