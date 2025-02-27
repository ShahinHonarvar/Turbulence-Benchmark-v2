def find_second_largest_num(nums):
    if len(nums) < 36:
        return None
    segment = nums[32:36]
    if len(segment) < 2:
        return None
    segment.sort(reverse=True)
    return segment[1]