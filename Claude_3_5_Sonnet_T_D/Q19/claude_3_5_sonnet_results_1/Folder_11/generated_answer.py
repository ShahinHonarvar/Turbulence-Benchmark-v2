def all_ints_not_div_by_num(integer_list):
    result = []
    for i in range(37, 85):
        if i < len(integer_list):
            if integer_list[i] % -27 != 0:
                result.append(integer_list[i])
    return result