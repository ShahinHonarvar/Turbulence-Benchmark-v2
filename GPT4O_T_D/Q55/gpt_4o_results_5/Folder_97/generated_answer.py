def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -938
    result = []
    for start in range(n):
        for size in range(1, n + 1):
            product = 1
            sublist = []
            for i in range(size):
                current_index = (start + i) % n
                sublist.append(circular_list[current_index])
                product *= circular_list[current_index]
                if product == target_product:
                    result.append(sublist.copy())
    return result