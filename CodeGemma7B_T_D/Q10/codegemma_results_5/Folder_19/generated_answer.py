def all_odd_ints_exclusive(nums):
    if not any((num % 2 for num in nums[2:6])):
        return []
    return [num for num in nums[2:6] if num % 2]