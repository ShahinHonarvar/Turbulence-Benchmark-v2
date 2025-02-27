def all_ints_div_by_num(int_list):
    return [num for idx, num in enumerate(int_list) if idx >= 40 and idx <= 400 and (num % 7 == 0)]