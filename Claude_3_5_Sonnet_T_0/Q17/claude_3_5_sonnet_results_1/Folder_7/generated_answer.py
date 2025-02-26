def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for i in range(543, 585):
        if i < len(integer_list):
            if integer_list[i] % -553 == 0 and integer_list[i] % -737 == 0:
                result.append(integer_list[i])
    return result