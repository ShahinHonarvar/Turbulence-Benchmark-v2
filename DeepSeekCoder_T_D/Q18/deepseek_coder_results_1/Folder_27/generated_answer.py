def sum_ints_div_by_either_nums(int_list):
    sum_divisible = 0
    for num in int_list[20:36]:
        if num % -36 == 0 or num % -89 == 0:
            sum_divisible += num
    return sum_divisible