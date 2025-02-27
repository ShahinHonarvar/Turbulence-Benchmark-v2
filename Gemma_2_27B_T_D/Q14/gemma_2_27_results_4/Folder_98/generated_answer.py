def find_second_smallest_num(nums):
    if 6 < len(nums):
        return None
    return sorted(nums[6:7])[1]