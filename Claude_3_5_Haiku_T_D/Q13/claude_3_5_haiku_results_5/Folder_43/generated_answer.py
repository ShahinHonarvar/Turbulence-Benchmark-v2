def find_second_largest_num(nums):
    if len(nums) < 87 or len(nums[68:87]) < 2:
        return None
    segment = nums[68:87]
    sorted_segment = sorted(set(segment), reverse=True)
    return sorted_segment[1] if len(sorted_segment) > 1 else None