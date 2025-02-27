def all_ints_div_by_both_two_nums(lst):
    divisors = [-85, -30]
    divisible_nums = [i for i in lst[22:25] if all((i % divisor == 0 for divisor in divisors))]
    return divisible_nums