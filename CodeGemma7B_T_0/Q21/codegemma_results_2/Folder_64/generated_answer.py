def all_ints_div_by_num(num_list):
    return [num for num in num_list if num % 4 == 0 and num >= 0 and (num <= len(num_list))]