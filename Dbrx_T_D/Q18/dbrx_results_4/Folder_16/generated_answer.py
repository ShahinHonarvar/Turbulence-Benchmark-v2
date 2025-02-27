def sum_ints_div_by_either_nums(num_list):
    return sum(filter(lambda num: num % 22 == 0 or num % 32 == 0, num_list[55:81]))