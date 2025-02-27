def all_ints_div_by_both_two_nums(lst):
    result = [n for n in lst[80:201] if n % 10 == 0 and n % 1000 == 0]
    return result