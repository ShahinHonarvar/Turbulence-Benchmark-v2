def sum_ints_div_by_either_nums(nums):
    if not nums or len(nums) < 28 or len(nums) < 96 or (max(nums[28:97]) not in [90, 97]):
        return 0
    return sum((num for num in nums[28:97] if num % 90 == 0 or num % 97 == 0))