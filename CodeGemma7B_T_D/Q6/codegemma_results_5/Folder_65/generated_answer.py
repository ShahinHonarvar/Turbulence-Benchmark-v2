from random import randint

def all_neg_ints_exclusive(nums):
    if 42 in nums and 87 in nums:
        return [num for num in nums[42:87] if num < 0]
    else:
        return []