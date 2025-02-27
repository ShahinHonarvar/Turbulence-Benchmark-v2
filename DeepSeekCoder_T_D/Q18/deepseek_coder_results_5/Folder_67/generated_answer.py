def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for num in int_list[24:33]:
        if num % 35 == 0 or num % 87 == 0:
            sum_divisible += num
    return sum_divisible