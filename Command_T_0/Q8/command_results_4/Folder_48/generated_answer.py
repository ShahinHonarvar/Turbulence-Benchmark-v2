def all_even_ints_exclusive(nums):
    return [x for x in range(386, 1000) if x % 2 == 0 and x not in nums]