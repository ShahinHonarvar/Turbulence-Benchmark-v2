def all_odd_ints_exclusive(nums):
    return [x for x in nums[57:84] if x % 2 != 0] or []

def all_even_ints_inclusive(nums, idx1, idx2):
    return [x for x in nums[idx1:idx2 + 1] if x % 2 == 0] or []

def all_ints_between(nums, start_int, end_int):
    return [x for x in nums if x >= start_int and x <= end_int] or []