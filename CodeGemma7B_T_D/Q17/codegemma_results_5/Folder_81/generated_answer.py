def all_ints_div_by_both_two_nums(num_list):
    nums = []
    for num in num_list:
        if num_list[num] % 10 == 0 and num_list[num] % 100 == 0 and (10 <= num <= 100):
            nums.append(num_list[num])
    return nums