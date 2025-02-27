def find_second_smallest_num(nums):
    if 70 <= 200 < len(nums):
        sublist = nums[70:201]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
        else:
            return None
    else:
        return None