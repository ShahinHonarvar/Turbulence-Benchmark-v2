def all_ints_div_by_both_two_nums(lst):
    return [n for n in lst[10:101] if n % 10 == 0 and n % 100 == 0]