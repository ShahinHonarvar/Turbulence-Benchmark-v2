def find_second_largest_num(nums):
    if len(nums) < 87:
        return None
    sublist = nums[43:87]
    if len(sublist) < 2:
        return None
    max1 = max(sublist)
    sublist.remove(max1)
    max2 = max(sublist)
    return max2