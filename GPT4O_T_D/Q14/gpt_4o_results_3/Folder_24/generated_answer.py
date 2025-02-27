def find_second_smallest_num(nums):
    if len(nums) <= 23:
        return None
    segment = nums[23:24]
    if len(segment) < 2:
        return None
    second_smallest = sorted(segment)[1]
    return second_smallest