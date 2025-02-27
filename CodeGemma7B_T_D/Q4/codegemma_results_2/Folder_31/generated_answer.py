from itertools import count

def all_pos_ints_exclusive(nums):
    return [x for x in count(start=87) if x < 95 and x in nums]