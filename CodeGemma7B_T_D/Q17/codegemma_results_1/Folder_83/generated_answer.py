def all_ints_div_by_both_two_nums(num_list):
    return [num for idx, num in enumerate(num_list) if idx >= 90 and idx <= 200 and (num % 31 == 0) and (num % 13 == 0)]