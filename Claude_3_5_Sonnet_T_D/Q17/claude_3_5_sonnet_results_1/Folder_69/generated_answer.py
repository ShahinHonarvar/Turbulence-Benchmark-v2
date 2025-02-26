def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for i in range(61, 89):
        if i < len(integer_list):
            if integer_list[i] % 31 == 0 and integer_list[i] % 11 == 0:
                result.append(integer_list[i])
    return result