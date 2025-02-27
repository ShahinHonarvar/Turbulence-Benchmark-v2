def all_odd_ints_exclusive(nums):
    return [x for x in nums if x % 2 and x in range(0, 3)]