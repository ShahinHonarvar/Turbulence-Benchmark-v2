def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for size in range(1, n + 1):
            current_index = (start + size - 1) % n
            product *= circular_list[current_index]
            if product == 29:
                sublist = []
                for k in range(size):
                    sublist.append(circular_list[(start + k) % n])
                result.append(sublist)
            if product == 0 or size == n:
                break
    return result