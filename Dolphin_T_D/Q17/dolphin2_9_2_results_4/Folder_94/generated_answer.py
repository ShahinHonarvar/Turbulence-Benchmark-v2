def all_ints_div_by_both_two_nums(nums):
    range_nums = nums[93:95]
    divisible_by_both = []
    for num in range_nums:
        if num % -53 == 0 and num % -91 == 0:
            divisible_by_both.append(num)
    return divisible_by_both