def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[20:36]:
        if num % -36 == 0 and num % -89 == 0:
            result.append(num)
    return result