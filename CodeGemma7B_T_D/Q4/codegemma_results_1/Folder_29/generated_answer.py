import itertools

def all_pos_ints_exclusive(nums):
    result = itertools.dropwhile(lambda n: n <= 0 or n > 76, nums[48:])
    return list(result) if any(result) else []