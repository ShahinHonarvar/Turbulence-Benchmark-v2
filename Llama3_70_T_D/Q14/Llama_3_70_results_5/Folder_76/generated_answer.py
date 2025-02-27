def find_second_smallest_num(nums):
    if len(nums[533:606]) < 2:
        return None
    return sorted(nums[533:606])[1]