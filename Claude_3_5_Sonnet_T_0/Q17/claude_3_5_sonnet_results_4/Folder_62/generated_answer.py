def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[44:60]:
        if num % 39 == 0 and num % 15 == 0:
            result.append(num)
    return result