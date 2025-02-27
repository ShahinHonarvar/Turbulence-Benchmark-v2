def all_ints_div_by_both_two_nums(lst):
    result = [lst[i] for i in range(54, 80) if lst[i] % 54 == 0 and lst[i] % 28 == 0]
    return result