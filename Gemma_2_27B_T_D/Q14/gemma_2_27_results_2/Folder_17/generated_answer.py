def find_second_smallest_num(nums):
    if len(nums[28:39]) < 2:
        return None
    return sorted(nums[28:39])[1]