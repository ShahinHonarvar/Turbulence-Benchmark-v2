def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[50:93]:
        if num % -94 == 0 and num % -95 == 0:
            result.append(num)
    return result