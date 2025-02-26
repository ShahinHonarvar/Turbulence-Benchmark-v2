def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[48:60]:
        if num % 88 == 0 and num % 58 == 0:
            result.append(num)
    return result