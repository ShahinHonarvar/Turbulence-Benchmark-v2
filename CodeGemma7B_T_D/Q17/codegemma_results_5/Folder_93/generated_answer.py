def all_ints_div_by_both_two_nums(nums):
    nums_divisible_by_both_two_nums = []
    for num in nums[86:89 + 1]:
        if num % -61 == 0 and num % -79 == 0:
            nums_divisible_by_both_two_nums.append(num)
    return nums_divisible_by_both_two_nums