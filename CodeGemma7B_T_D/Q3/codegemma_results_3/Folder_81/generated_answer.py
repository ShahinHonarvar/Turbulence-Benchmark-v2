def all_pos_ints_inclusive(nums):
    if not any((n > 0 for n in nums)):
        return []
    return [i for i in range(10, 101) if i in nums]