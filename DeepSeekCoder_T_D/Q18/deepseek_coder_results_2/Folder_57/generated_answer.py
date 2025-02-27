def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[51:77]:
        if num % -90 == 0 or num % -59 == 0:
            total += num
    return total