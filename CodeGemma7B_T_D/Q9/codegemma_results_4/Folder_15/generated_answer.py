def all_odd_ints_inclusive(nums):
    if not any((num % 2 for num in nums[0:4])):
        return []
    return [num for num in nums[0:4] if num % 2]