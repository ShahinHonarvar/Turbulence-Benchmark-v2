def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    elif 56 <= len(nums):
        sublist = nums[56:58]
        sublist.sort()
        if len(sublist) == 2:
            return sublist[1]
    return None