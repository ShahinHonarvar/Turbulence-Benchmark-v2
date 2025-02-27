def find_second_smallest_num(nums):
    specified_range = nums[32:36]
    if len(specified_range) < 2:
        return None
    return sorted(specified_range)[1]