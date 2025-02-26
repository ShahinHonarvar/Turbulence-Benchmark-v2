def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for i in range(50, 93):
        if i < len(integer_list):
            if integer_list[i] % -94 == 0 and integer_list[i] % -95 == 0:
                result.append(integer_list[i])
    return result