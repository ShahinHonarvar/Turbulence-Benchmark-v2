def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[:6]:
        if num % -1 == 0 and num % 13 == 0:
            result.append(num)
    return result