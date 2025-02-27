def all_ints_div_by_both_two_nums(l):
    divisible = [i for i in l[:4] if i % 11 == 0 and i % -7 == 0]
    return divisible