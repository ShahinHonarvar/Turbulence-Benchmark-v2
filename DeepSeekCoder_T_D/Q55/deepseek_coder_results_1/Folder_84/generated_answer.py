def lists_with_product_equal_n(circular_list):
    target_product = -906
    result = []
    n = len(circular_list)
    for start in range(n):
        current_product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            current_product *= circular_list[index]
            sublist.append(circular_list[index])
            if current_product == target_product:
                result.append(sublist.copy())
            if current_product == 0 or current_product == target_product:
                break
        if current_product == target_product:
            continue
        current_product = 1
        sublist = []
        for i in range(n - 1, -1, -1):
            index = (start + i) % n
            current_product *= circular_list[index]
            sublist.append(circular_list[index])
            if current_product == target_product:
                result.append(sublist.copy())
            if current_product == 0 or current_product == target_product:
                break
    return result