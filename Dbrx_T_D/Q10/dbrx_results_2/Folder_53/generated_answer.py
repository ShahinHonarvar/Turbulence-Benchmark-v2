def all_odd_ints_exclusive(nums):
    if len(nums) < 102:
        return []
    return [num for num in nums[100:102] if num % 2 != 0]