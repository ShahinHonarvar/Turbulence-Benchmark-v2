def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for num in int_list[10:29]:
        if num % -61 == 0 or num % -64 == 0:
            sum_divisible += num
    return sum_divisible