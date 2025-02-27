def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[38:82]:
        if num % -61 == 0 or num % -71 == 0:
            total += num
    return total