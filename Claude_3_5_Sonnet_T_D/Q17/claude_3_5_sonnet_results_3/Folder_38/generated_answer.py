def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[10:77]:
        if num % -40 == 0 and num % -12 == 0:
            result.append(num)
    return result