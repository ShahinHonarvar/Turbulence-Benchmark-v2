def all_ints_div_by_both_two_nums(lst):
    divisible_ints = []
    for num in lst[22:25]:
        if num % -85 == 0 and num % -30 == 0:
            divisible_ints.append(num)
    return divisible_ints