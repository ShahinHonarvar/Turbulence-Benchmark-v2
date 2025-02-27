def all_ints_div_by_num(integer_list):
    result = []
    for i in range(len(integer_list)):
        if i >= 12 and i <= 15 and (integer_list[i] % -80 == 0):
            result.append(integer_list[i])
    return result