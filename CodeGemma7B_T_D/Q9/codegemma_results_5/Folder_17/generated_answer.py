def all_odd_ints_inclusive(nums):
    if not any((num % 2 for num in nums[62:79])):
        return []
    return [num for num in nums[62:79] if num % 2]