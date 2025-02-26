def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for i in range(min(6, len(integer_list))):
        if integer_list[i] % -1 == 0 and integer_list[i] % 13 == 0:
            result.append(integer_list[i])
    return result