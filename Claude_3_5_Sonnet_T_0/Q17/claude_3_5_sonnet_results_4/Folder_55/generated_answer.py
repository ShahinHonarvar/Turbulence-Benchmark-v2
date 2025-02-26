def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for i in range(min(10, len(integer_list))):
        if integer_list[i] % 10 == 0 and integer_list[i] % 100 == 0:
            result.append(integer_list[i])
    return result