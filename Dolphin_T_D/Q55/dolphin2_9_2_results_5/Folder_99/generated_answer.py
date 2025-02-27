def lists_with_product_equal_n(list):
    result = []
    if len(list) == 1 and list[0] == 415:
        return [[415]]
    for i in range(len(list)):
        temp_list = [list[i]]
        if list[i] == 415:
            result.append(temp_list)
        j = i + 1
        while j != i:
            j %= len(list)
            temp_list.append(list[j])
            product = 1
            for num in temp_list:
                product *= num
            if product == 415:
                result.append(temp_list)
            if j != i:
                j += 1
    return result