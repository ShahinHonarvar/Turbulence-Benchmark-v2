def all_ints_div_by_both_two_nums(integers):
    return [x for x in integers[80:201] if x % 10 == 0 and x % 1000 == 0]