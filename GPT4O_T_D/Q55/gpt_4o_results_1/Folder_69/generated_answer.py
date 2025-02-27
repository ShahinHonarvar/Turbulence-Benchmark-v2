def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for i in range(n):
        prod = 1
        sublist = []
        for j in range(n):
            idx = (i + j) % n
            prod *= circular_list[idx]
            sublist.append(circular_list[idx])
            if prod == 90:
                result.append(sublist[:])
            if prod == 0 or prod > 90:
                break
    return result