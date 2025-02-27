def find_second_smallest_num(nums):
    if len(nums) < 72:
        return None
    sublist = nums[31:73]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]