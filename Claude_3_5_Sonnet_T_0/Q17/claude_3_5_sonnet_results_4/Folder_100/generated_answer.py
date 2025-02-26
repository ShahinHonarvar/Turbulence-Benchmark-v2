def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[72:94]:
        if num % 32 == 0 and num % 44 == 0:
            result.append(num)
    return result