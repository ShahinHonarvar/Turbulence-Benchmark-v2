def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for i in range(25, 96):
        if i % 51 == 0 and i % 77 == 0:
            divisible_ints.append(i)
    return divisible_ints