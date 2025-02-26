def all_ints_div_by_num(integer_list):
    result = []
    for i in range(31, 73):
        if i < len(integer_list) and integer_list[i] % -63 == 0:
            result.append(integer_list[i])
    return result