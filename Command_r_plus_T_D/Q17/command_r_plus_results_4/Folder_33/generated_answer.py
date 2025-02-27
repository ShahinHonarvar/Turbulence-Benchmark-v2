def all_ints_div_by_both_two_nums(lst):
    divisor_1 = -722
    divisor_2 = -731
    start_index = 281
    end_index = 694
    divisible_nums = []
    for i in range(start_index, end_index + 1):
        if lst[i] % divisor_1 == 0 and lst[i] % divisor_2 == 0:
            divisible_nums.append(lst[i])
    return divisible_nums