def find_second_largest_num(nums):
    segment = nums[15:52]
    if len(segment) < 2:
        return None
    return sorted(segment)[-2]