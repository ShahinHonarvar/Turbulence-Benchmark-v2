def find_second_smallest_num(nums):
    segment = nums[70:201]
    if len(segment) < 2:
        return None
    segment_sorted = sorted(segment)
    return segment_sorted[1]