def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[51:77]:
        if num % -90 == 0 and num % -59 == 0:
            result.append(num)
    return result