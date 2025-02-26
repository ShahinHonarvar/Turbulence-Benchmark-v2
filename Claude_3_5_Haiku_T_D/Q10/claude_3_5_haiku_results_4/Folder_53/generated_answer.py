def all_odd_ints_exclusive(nums):
    if len(nums) <= 102:
        return []
    return [num for num in nums[101:-1] if num % 2 != 0]