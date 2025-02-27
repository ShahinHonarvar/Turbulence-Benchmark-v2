def all_pos_ints_exclusive(nums):
    if not any((i > 0 for i in nums[361:643])):
        return []
    return [i for i in nums[361:643] if i > 0]