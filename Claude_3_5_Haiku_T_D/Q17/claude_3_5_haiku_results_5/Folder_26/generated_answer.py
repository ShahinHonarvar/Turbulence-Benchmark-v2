def all_ints_div_by_both_two_nums(num_list):
    divisible_nums = []
    for num in num_list[69:71]:
        if num % 72 == 0 and num % 70 == 0:
            divisible_nums.append(num)
    return divisible_nums