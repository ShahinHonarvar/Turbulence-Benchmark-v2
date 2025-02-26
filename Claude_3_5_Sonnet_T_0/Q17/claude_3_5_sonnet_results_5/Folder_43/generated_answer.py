def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[57:86]:
        if num % -77 == 0 and num % -32 == 0:
            result.append(num)
    return result