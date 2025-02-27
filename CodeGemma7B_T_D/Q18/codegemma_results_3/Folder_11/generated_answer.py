def sum_ints_div_by_either_nums(int_list):
    result = 0
    for num in int_list[22:25]:
        if num % -85 == 0 or num % -30 == 0:
            result += num
    return result