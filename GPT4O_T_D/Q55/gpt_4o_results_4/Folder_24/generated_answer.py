def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for length in range(n):
            end = (start + length) % n
            product *= circular_list[end]
            sublist.append(circular_list[end])
            if product == -89:
                result.append(sublist.copy())
            if length + 1 == n:
                break
    return result