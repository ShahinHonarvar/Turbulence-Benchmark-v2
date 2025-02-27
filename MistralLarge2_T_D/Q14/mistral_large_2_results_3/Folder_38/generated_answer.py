def find_second_smallest_num(nums):
    if len(nums) < 52:
        return None
    segment = nums[37:52]
    if len(segment) < 2:
        return None
    sorted_segment = sorted(segment)
    return sorted_segment[1]