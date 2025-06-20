def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -51
    result = []
    for start in range(n):
        current_product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            current_product *= circular_list[index]
            sublist.append(circular_list[index])
            if current_product == target_product:
                result.append(sublist.copy())
            if current_product == 0 or current_product % target_product == 0:
                continue
            else:
                break
        if current_product == target_product:
            for j in range(1, len(sublist)):
                sub = sublist[j:]
                if len(sub) > 0:
                    result.append(sub)
    return result