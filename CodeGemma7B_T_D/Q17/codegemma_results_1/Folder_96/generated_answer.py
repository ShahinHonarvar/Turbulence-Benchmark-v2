def all_ints_div_by_both_two_nums(int_list):
    filtered_list = filter(lambda x: x % 34 == 0 and x % 64 == 0 and (50 <= x <= 200), int_list)
    return list(filtered_list)