def all_ints_div_by_num(integer_list):
    result = []
    for i in range(66, 82):
        if i < len(integer_list) and integer_list[i] % 77 == 0:
            result.append(integer_list[i])
    return result