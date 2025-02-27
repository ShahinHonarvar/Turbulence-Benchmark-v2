def all_ints_div_by_both_two_nums(int_list):
    divisible_by_both = []
    for i in range(54, 80):
        if i in int_list and i % 54 == 0 and (i % 28 == 0):
            divisible_by_both.append(i)
    return divisible_by_both