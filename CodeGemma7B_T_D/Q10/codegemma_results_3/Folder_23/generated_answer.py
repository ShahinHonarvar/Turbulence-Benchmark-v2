def all_odd_ints_exclusive(nums):
    if all((num % 2 == 0 for num in nums)):
        return []
    return [num for num in nums if num % 2 != 0 and 29 < num < 53]