def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[11:77]:
        if num % -81 == 0 or num % -94 == 0:
            total += num
    return total