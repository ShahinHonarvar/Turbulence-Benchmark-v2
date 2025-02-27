def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        current_sublist = []
        for length in range(1, n + 1):
            index = (start + length - 1) % n
            product *= circular_list[index]
            current_sublist.append(circular_list[index])
            if product == -81:
                result.append(current_sublist.copy())
            if length == n:
                break
    return result