def all_ints_div_by_num(list_of_nums):
    divisible_nums = []
    if len(list_of_nums) > 0:
        if list_of_nums[0] % 6 == 0:
            divisible_nums.append(list_of_nums[0])
    return divisible_nums