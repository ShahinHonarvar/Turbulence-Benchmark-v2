def lists_with_product_equal_n(circular_list):
    target_product = -65
    result = []
    n = len(circular_list)
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target_product:
                result.append(sublist[:])
            if len(sublist) == n:
                break
    return result