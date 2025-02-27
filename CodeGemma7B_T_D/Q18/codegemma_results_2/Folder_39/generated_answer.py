def sum_ints_div_by_either_nums(num_list):
    return sum([num for num in num_list[13:77] if num % 66 == 0 or num % 32 == 0]) or 0