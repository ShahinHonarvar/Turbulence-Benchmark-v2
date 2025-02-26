def all_ints_div_by_both_two_nums(int_list):
    result = []
    for num in int_list[29:54]:
        if num % -68 == 0 and num % -85 == 0:
            result.append(num)
    return result