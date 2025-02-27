def all_ints_not_div_by_num(integer_list):
    for i in range(0, 2):
        if len(integer_list) > i and integer_list[i] % -2 == 0:
            return [j for j in integer_list if j % -2 != 0]
    return integer_list[0:2] if len(integer_list) > 1 else integer_list if integer_list[0] % -2 != 0 else []