def all_ints_div_by_both_two_nums(lst):
    divisible_by_both = []
    for i in range(10):
        if lst[i] % 10 == 0 and lst[i] % 100 == 0:
            divisible_by_both.append(lst[i])
    return divisible_by_both