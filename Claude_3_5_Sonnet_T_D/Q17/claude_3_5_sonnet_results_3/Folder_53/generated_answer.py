def all_ints_div_by_both_two_nums(integer_list):
    result = []
    if len(integer_list) > 200:
        num = integer_list[200]
        if num % 17 == 0 and num % -5 == 0:
            result.append(num)
    return result