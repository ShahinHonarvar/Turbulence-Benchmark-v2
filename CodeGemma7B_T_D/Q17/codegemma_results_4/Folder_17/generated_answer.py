def all_ints_div_by_both_two_nums(list_of_ints):
    divisible_nums = []
    for num in list_of_ints[81:89 + 1]:
        if num % 56 == 0 and num % 68 == 0:
            divisible_nums.append(num)
    return divisible_nums