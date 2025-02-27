def all_ints_div_by_both_two_nums(lst):
    both_divisible = []
    for i in range(10, 76):
        if i in lst and i % -40 == 0 and (i % -12 == 0):
            both_divisible.append(i)
    return both_divisible