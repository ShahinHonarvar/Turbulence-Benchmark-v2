def find_second_smallest_num(nums):
    if 200 < len(nums) - 1:
        return None
    elif 30 > len(nums) - 1:
        return None
    else:
        sublist = nums[30:201]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]