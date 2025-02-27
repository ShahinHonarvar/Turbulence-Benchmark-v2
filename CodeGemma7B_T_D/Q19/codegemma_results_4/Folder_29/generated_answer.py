def all_ints_not_div_by_num(nums):
    not_divisible_nums = []
    for num in nums[24:25]:
        if num % -30 != 0:
            not_divisible_nums.append(num)
    return not_divisible_nums