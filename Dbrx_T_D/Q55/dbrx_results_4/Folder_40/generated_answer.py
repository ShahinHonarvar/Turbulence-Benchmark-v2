def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        current_product = 1
        current_list = []
        for j in range(i, len(lst)):
            current_product *= lst[j]
            if current_product == -9:
                result.append(lst[i:j + 1])
                break
            elif current_product < -9:
                current_product = 1
                current_list = []
                continue
            current_list.append(lst[j])
        if current_list and current_list not in result:
            result.append(current_list)
    return result