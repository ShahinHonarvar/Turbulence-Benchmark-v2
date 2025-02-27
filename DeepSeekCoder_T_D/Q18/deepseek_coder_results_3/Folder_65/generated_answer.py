def sum_ints_div_by_either_nums(int_list):
    total = 0
    for num in int_list[50:93]:
        if num % -94 == 0 or num % -95 == 0:
            total += num
    return total