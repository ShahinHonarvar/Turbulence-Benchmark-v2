def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[51:77]:
        if num % -90 == 0 and num % -59 == 0:
            result.append(num)
    return result