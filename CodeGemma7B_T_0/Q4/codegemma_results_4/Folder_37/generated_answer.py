def all_pos_ints_exclusive(nums):
    return [num for num in range(1, len(nums)) if num not in nums]