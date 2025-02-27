def find_second_smallest_num(nums):
    if len(nums) < 5:
        return None
    else:
        sublist = nums[3:6]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]