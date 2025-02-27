def find_second_smallest_num(nums):
    if len(nums) < 80:
        return None
    else:
        sublist = nums[29:80]
        if len(sublist) < 2:
            return None
        else:
            sublist.sort()
            return sublist[1]