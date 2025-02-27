def lists_with_product_equal_n(circular_list):
    target_product = -97
    n = len(circular_list)
    results = []
    for start in range(n):
        current_product = 1
        current_list = []
        for i in range(n):
            index = (start + i) % n
            current_list.append(circular_list[index])
            current_product *= circular_list[index]
            if current_product == target_product:
                results.append(current_list[:])
            if len(current_list) == n:
                break
    return results