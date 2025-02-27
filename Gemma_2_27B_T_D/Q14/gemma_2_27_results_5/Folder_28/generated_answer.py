def find_second_smallest_num(nums):
    if len(nums[22:51]) < 2:
        return None
    return sorted(nums[22:51])[1]