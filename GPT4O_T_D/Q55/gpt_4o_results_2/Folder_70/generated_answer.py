def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        temp_sublist = []
        for offset in range(n):
            index = (start + offset) % n
            product *= circular_list[index]
            temp_sublist.append(circular_list[index])
            if product == 32:
                result.append(temp_sublist[:])
                break
            if product > 32 or offset == n - 1:
                break
    return result