def find_second_largest_num(nums):
    specified_range = nums[31:73]
    if len(specified_range) < 2:
        return None
    return sorted(specified_range)[-2]