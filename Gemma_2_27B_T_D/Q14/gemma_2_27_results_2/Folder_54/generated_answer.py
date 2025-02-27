def find_second_smallest_num(nums):
    if len(nums[68:87]) < 2:
        return None
    return sorted(nums[68:87])[1]