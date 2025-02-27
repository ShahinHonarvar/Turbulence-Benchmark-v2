def find_second_smallest_num(nums):
    if len(nums[:2]) < 2:
        return None
    return max(min(nums[0], nums[1]), min(nums[1], nums[0]))