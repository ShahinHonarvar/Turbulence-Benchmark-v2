def find_second_smallest_num(nums):
    if len(nums) < 9:
        return None
    sublist = nums[8:10]
    if len(sublist) < 2:
        return None
    return sorted(sublist)[1]