def all_ints_not_div_by_num(integer_list):
    result = []
    for i in range(1, 7):
        if i < len(integer_list) and integer_list[i] % 7 != 0:
            result.append(integer_list[i])
    return result