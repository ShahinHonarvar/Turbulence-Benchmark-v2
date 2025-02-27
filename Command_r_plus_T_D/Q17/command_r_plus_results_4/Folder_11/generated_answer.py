def all_ints_div_by_both_two_nums(lst):
    divisors = [-85, -30]
    divisible_nums = []
    for i in range(22, 25):
        if lst[i] % divisors[0] == 0 and lst[i] % divisors[1] == 0:
            divisible_nums.append(lst[i])
    return divisible_nums