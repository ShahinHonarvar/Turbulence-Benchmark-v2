def all_odd_ints_exclusive(nums):
    if not any((num % 2 for num in nums[36:54])):
        return []
    return [num for num in nums[36:54] if num % 2]