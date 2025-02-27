def all_odd_ints_exclusive(nums):
    odd_nums = [num for num in nums[10:75] if num % 2 != 0]
    return odd_nums or []