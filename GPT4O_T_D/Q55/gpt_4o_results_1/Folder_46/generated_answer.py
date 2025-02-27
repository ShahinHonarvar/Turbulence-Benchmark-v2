def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    for i in range(n):
        product = 1
        sublist = []
        for j in range(n):
            idx = (i + j) % n
            product *= circular_list[idx]
            sublist.append(circular_list[idx])
            if product > 53:
                break
            if product == 53:
                result.append(sublist[:])
                break
    return result