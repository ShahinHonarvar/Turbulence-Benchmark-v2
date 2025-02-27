def find_second_smallest_num(nums):
    if len(nums) < 87:
        return None
    sublist = sorted(nums[43:87])
    if len(sublist) < 2:
        return None
    return sublist[1]