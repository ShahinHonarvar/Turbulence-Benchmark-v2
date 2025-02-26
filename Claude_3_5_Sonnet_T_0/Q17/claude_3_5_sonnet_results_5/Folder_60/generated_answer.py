def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[10:80]:
        if num % -74 == 0 and num % -58 == 0:
            result.append(num)
    return result