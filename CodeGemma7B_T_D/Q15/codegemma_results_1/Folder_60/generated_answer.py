def sum_odd_ints_inclusive(nums):
    if not any((n % 2 for n in nums[75:86])):
        return 0
    return sum([n for n in nums[75:86] if n % 2])