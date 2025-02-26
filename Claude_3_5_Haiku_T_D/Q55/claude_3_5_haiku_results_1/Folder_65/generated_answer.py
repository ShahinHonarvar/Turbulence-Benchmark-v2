def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            current_sublist = []
            product = 1
            for i in range(length):
                index = (start + i) % n
                current_sublist.append(circular_list[index])
                product *= circular_list[index]
            if product == 46:
                result.append(current_sublist)
    return result