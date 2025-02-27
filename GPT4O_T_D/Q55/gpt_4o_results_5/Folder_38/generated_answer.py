def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for offset in range(n):
            index = (start + offset) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if len(sublist) <= n and product == -23:
                result.append(sublist[:])
    return result