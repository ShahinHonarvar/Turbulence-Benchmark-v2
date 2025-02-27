def all_ints_div_by_both_two_nums(l):
    divisible_by_both = []
    for i in range(56, 89):
        if l[i] % -59 == 0 and l[i] % -79 == 0:
            divisible_by_both.append(l[i])
    return divisible_by_both