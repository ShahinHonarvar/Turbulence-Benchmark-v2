def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for i in range(57, 86):
        if i < len(integer_list):
            if integer_list[i] % -77 == 0 and integer_list[i] % -32 == 0:
                result.append(integer_list[i])
    return result