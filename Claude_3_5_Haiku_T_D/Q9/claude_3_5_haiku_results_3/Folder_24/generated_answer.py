def all_odd_ints_inclusive(nums):
    if len(nums) <= 95:
        return []
    return [num for num in nums[74:96] if num % 2 != 0]