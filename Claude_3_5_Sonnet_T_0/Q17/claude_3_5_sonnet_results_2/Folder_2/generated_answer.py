def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[73:87]:
        if num % 54 == 0 and num % 82 == 0:
            result.append(num)
    return result