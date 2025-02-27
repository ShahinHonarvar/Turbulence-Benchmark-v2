def find_second_smallest_num(nums):
    if len(nums[43:87]) < 2:
        return None
    return sorted(nums[43:87])[1]