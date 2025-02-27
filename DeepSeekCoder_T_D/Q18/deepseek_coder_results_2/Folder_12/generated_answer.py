def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[35:65]:
        if num % -30 == 0 or num % -95 == 0:
            total += num
    return total