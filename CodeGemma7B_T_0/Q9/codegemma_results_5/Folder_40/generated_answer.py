def all_odd_ints_inclusive(nums):
    if not any((num % 2 for num in nums)):
        return []
    return [num for num in nums if num % 2 != 0]