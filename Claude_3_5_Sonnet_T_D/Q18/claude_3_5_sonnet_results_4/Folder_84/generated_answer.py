def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[78:82] if num % 76 == 0 or num % 60 == 0))