def all_pos_ints_inclusive(nums):
    if not any((num > 0 for num in nums[40:201])):
        return []
    pos_ints = [num for num in nums[40:201] if num > 0]
    pos_ints.sort()
    return pos_ints