def find_second_largest_num(nums):
    if len(nums[100:201]) < 2:
        return None
    return sorted(nums[100:201])[-2]