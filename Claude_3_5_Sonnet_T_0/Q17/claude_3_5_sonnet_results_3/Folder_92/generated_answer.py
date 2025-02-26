def all_ints_div_by_both_two_nums(integer_list):
    result = []
    if integer_list:
        if integer_list[0] % 1 == 0 and integer_list[0] % -1 == 0:
            result.append(integer_list[0])
    return result