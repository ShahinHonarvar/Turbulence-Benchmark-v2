def sum_ints_div_by_either_nums(int_list):
    valid_range = int_list[1:5]
    return sum((num for num in valid_range if num % 4 == 0 or num % -6 == 0))