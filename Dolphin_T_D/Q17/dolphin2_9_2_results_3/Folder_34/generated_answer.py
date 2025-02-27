def all_ints_div_by_both_two_nums(l):
    divisible_ints = []
    for i in range(60, 201):
        if i % 9 == 0 and i % 11 == 0:
            divisible_ints.append(i)
    return divisible_ints