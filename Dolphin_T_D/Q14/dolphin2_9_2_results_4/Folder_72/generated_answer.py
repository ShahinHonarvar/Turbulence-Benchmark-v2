def find_second_smallest_num(nums):
    if len(nums) < 86:
        return None
    else:
        sublist = nums[82:87]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]