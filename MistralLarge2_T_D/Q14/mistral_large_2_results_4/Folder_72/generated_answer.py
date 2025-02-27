def find_second_smallest_num(nums):
    if len(nums) < 87:
        return None
    sublist = nums[82:87]
    if len(sublist) < 2:
        return None
    sorted_sublist = sorted(sublist)
    return sorted_sublist[1]