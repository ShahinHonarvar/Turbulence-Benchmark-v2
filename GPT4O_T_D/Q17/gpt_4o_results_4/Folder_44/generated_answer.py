def all_ints_div_by_both_two_nums(int_list):
    result = [n for n in int_list[25:71] if n % 74 == 0 and n % 15 == 0]
    return result