def find_second_smallest_num(nums):
    if len(nums) < 87:
        return None
    sublist = nums[68:87]
    if len(sublist) < 2:
        return None
    first_min = min(sublist)
    sublist.remove(first_min)
    second_min = min(sublist)
    return second_min