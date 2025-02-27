def sum_ints_div_by_either_nums(list_num):
    sum_nums = 0
    for num in list_num[73:87]:
        if num % 54 == 0 or num % 82 == 0:
            sum_nums += num
    return sum_nums