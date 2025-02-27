def find_second_smallest_num(nums):
    if len(nums[30:201]) < 2:
        return None
    return sorted(nums[30:201])[1]