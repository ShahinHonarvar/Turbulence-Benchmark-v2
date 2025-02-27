def all_odd_ints_inclusive(nums):
    if not any((num % 2 != 0 for num in nums[91:99])):
        return []
    return [num for num in nums[91:99] if num % 2 != 0]