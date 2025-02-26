def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[35:65]:
        if num % -30 == 0 and num % -95 == 0:
            result.append(num)
    return result