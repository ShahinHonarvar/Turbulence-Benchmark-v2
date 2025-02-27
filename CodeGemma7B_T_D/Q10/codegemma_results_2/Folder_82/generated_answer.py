def all_odd_ints_exclusive(nums):
    if all((i % 2 == 0 for i in nums)):
        return []
    return [num for num in nums if num % 2 != 0 and num > 20 and (num < 200)]