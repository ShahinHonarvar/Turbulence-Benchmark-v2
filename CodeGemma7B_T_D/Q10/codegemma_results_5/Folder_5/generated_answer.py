def all_odd_ints_exclusive(nums):
    if not nums or nums[2] % 2 == 0 or nums[7] % 2 == 0:
        return []
    return [num for num in nums[2:7] if num % 2 != 0]