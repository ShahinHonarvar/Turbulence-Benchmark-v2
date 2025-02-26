def find_second_smallest_num(nums):
    if len(nums) <= 23:
        return None
    segment = nums[23:24]
    if not segment:
        return None
    return segment[0]