def find_second_largest_num(nums):
    if len(nums) < 87:
        return None
    sublist = nums[82:87]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]