def find_second_largest_num(nums):
    if len(nums) < 88:
        return None
    specified_range = nums[25:88]
    if len(specified_range) < 2:
        return None
    specified_range.sort(reverse=True)
    return specified_range[1]