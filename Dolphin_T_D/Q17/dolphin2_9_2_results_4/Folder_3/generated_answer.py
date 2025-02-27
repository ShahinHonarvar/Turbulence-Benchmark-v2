def all_ints_div_by_both_two_nums(ints):
    divisible_ints = []
    for i in range(38, 53):
        if i in ints and i % -41 == 0 and (i % -47 == 0):
            divisible_ints.append(i)
    return divisible_ints