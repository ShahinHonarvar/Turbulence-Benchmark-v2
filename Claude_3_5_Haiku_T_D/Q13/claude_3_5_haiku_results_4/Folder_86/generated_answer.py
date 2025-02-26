def find_second_largest_num(nums):
    if len(nums) < 35:
        return None
    segment = nums[31:35]
    if len(segment) < 2:
        return None
    sorted_segment = sorted(set(segment), reverse=True)
    return sorted_segment[1] if len(sorted_segment) > 1 else None