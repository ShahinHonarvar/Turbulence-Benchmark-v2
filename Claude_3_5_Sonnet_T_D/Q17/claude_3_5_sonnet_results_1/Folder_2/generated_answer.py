def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for i in range(73, 87):
        if i < len(integer_list):
            if integer_list[i] % 54 == 0 and integer_list[i] % 82 == 0:
                result.append(integer_list[i])
    return result