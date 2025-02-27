def all_odd_ints_inclusive(nums):
    if not nums or not any((num % 2 for num in nums)):
        return []
    return [num for num in nums if num % 2 != 0 and num in range(0, 7)]