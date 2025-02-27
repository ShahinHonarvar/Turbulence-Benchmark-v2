def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            j = (start + i) % n
            sublist.append(circular_list[j])
            product *= circular_list[j]
            if product == -23:
                result.append(sublist[:])
            if len(sublist) == n:
                break
    return result