def sum_ints_div_by_either_nums(int_list):
    target_range = int_list[77:88]
    return sum((num for num in target_range if num % 23 == 0 or num % 57 == 0))