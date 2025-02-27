def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for end in range(n):
            index = (start + end) % n
            sublist.append(circular_list[index])
            product *= circular_list[index]
            if product == -8:
                result.append(sublist[:])
            if end == n - 1:
                break
    return result