def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[29:54]:
        if num % -68 == 0 and num % -85 == 0:
            result.append(num)
    return result