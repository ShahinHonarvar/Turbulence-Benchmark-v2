def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    else:
        sublist = sorted(nums[5:8])
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]