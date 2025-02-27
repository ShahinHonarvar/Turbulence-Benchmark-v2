def all_ints_div_by_num(num_list):
    return [num for i, num in enumerate(num_list) if i <= 2 and num % 5 == 0]