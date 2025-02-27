def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 5:
        return []
    return [num for num in nums[1:5] if num % 4 == 0 and num % -6 == 0]