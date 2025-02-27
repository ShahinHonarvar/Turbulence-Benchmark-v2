def lists_with_product_equal_n(circular_list):
    target_product = -56
    n = len(circular_list)
    result = []
    for start in range(n):
        for length in range(1, n + 1):
            current_product = 1
            sublist = []
            for i in range(length):
                value = circular_list[(start + i) % n]
                sublist.append(value)
                current_product *= value
                if current_product == target_product:
                    result.append(sublist[:])
                    break
                if current_product == 0:
                    break
    return result