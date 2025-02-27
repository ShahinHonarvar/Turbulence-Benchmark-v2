def sum_ints_div_by_either_nums(lst):
    sum_num = 0
    for num in lst[137:425]:
        if num % -863 == 0 or num % -329 == 0:
            sum_num += num
    return sum_num if sum_num != 0 else 0