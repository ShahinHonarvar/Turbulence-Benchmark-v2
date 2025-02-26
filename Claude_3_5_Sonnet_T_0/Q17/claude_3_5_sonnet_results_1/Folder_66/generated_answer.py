def all_ints_div_by_both_two_nums(integer_list):
    result = []
    for num in integer_list[58:82]:
        if num % 55 == 0 and num % 10 == 0:
            result.append(num)
    return result