def all_odd_ints_exclusive(nums):
    if any((num % 2 != 0 and 43 < num < 99 for num in nums)):
        return [num for num in nums if num % 2 != 0 and 43 < num < 99]
    else:
        return []