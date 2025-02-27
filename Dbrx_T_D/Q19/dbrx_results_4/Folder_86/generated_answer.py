def all_ints_not_div_by_num(integer_list):
    result = []
    for i in range(15, 63):
        if integer_list[i] % 34 != 0:
            result.append(integer_list[i])
    return result