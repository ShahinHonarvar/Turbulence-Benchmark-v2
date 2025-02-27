def all_ints_div_by_both_two_nums(lst):
    selected_numbers = [i for i in lst[34:70] if i % 19 == 0 and i % 32 == 0]
    return selected_numbers