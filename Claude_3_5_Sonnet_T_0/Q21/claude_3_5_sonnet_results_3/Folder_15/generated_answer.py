def all_ints_div_by_num(integer_list):
    result = []
    if integer_list and integer_list[0] % 3 == 0:
        result.append(integer_list[0])
    return result