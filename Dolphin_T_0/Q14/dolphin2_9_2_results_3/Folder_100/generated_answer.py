def find_second_smallest_num(nums):
    if len(nums) < 52:
        return None
    else:
        sublist = nums[43:52]
        sublist = list(set(sublist))
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]