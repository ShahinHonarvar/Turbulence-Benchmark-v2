def lists_with_product_equal_n(list):
    length = len(list)
    lists = []
    for i in range(length):
        current_list = [list[i]]
        current_product = list[i]
        for j in range(i + 1, length):
            current_product *= list[j]
            current_list.append(list[j])
            if current_product == 28:
                lists.append(current_list[:])
            elif current_product > 28:
                break
    for i in range(length):
        current_list = [list[i]]
        current_product = list[i]
        for j in range(i - 1, -1, -1):
            current_product *= list[j]
            current_list.append(list[j])
            if current_product == 28:
                lists.append(current_list[:])
            elif current_product > 28:
                break
    return lists