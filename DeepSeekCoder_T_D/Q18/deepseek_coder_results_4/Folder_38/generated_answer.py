def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[10:77]:
        if num % -40 == 0 or num % -12 == 0:
            total += num
    return total