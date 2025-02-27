def all_ints_div_by_both_two_nums(int_list):
    divisible_ints = []
    for i in range(10, 80):
        if i % -74 == 0 and i % -58 == 0:
            divisible_ints.append(i)
    return divisible_ints