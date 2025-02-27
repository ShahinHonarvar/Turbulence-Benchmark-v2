def all_ints_div_by_both_two_nums(nums):
    res = [num for num in nums[81:89 + 1] if num % 56 == 0 and num % 68 == 0]
    return res if res else []