def find_second_smallest_num(nums):
    if len(nums[70:201]) < 2:
        return None
    return sorted(nums[70:201])[1]