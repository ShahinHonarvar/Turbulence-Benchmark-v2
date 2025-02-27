def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    target_product = -57
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
            if current_product == 0 or current_product == target_product:
                break
            if abs(current_product) > abs(target_product):
                break
        if current_product == target_product:
            for j in range(1, n):
                index = (start + j) % n
                sublist.pop(0)
                sublist.append(circular_list[index])
                current_product //= circular_list[(start + j - 1) % n]
                current_product *= circular_list[index]
                if current_product == target_product:
                    result.append(sublist.copy())
                if current_product == 0 or current_product == target_product:
                    break
                if abs(current_product) > abs(target_product):
                    break
    return result