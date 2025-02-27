def find_second_smallest_num(nums):
    if len(nums) > 87:
        sublist = nums[25:88]
        if len(sublist) >= 2:
            sublist.sort()
            return sublist[1]
    return None