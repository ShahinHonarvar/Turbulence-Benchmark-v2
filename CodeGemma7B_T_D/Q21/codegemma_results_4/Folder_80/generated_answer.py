import math

def all_ints_div_by_num(int_list):
    divisible_nums = []
    for num in int_list[27:87]:
        if num % 29 == 0:
            divisible_nums.append(num)
    return divisible_nums