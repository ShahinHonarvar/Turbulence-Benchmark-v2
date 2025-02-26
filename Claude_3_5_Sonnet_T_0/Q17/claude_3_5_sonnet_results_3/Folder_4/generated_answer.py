def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[86:91]:
        if num % -71 == 0 and num % -67 == 0:
            result.append(num)
    return result