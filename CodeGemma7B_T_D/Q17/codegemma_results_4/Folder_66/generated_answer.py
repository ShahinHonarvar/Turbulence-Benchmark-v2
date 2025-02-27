def all_ints_div_by_both_two_nums(int_list):
    divisible_nums = []
    for num in int_list[58:82]:
        if num % 55 == 0 and num % 10 == 0:
            divisible_nums.append(num)
    return divisible_nums