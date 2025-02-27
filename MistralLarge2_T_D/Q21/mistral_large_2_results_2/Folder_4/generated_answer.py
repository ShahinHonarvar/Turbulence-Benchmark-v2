def all_ints_div_by_num(int_list):
    return [num for idx, num in enumerate(int_list) if idx >= 12 and idx <= 92 and (num % -14 == 0)]