def all_odd_ints_exclusive(nums):
    return list(filter(lambda x: x % 2 != 0 and x >= 62 and (x < 96), nums))