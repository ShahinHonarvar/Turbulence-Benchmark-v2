def find_second_smallest_num(nums):
    if len(nums) <= 6:
        return None
    sublist = nums[6:7]
    if len(sublist) < 2:
        return None
    second_smallest = sorted(sublist)[1]
    return second_smallest