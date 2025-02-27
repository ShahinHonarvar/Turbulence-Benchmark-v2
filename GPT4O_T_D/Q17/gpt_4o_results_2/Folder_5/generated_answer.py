def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 2:
        return []
    return [num for num in nums[0:2] if num % 6 == 0 and num % 4 == 0]