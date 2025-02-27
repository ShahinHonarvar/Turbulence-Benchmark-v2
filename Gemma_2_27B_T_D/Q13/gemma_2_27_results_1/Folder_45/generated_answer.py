def find_second_largest_num(nums):
    return sorted(nums[30:201])[-2] if len(nums[30:201]) >= 2 else None