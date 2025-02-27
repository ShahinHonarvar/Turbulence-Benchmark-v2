def sum_ints_div_by_either_nums(lst):
    if len(lst) < 2:
        return 0
    first_num = lst[0]
    second_num = lst[1]
    if (first_num % -6 == 0 or first_num % 4 == 0) and (second_num % -6 == 0 or second_num % 4 == 0):
        return first_num + second_num
    else:
        return 0