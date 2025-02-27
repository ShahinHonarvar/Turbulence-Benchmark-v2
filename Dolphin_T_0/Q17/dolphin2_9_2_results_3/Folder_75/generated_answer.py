def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for i in range(20, 94):
        if i % -92 == 0 and i % -50 == 0:
            divisible_ints.append(i)
    return divisible_ints