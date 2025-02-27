def find_second_smallest_num(nums):
    if 750 >= len(nums) >= 246:
        sublist = nums[246:751]
        if len(set(sublist)) < 2:
            return None
        else:
            sublist.sort()
            return sublist[1]
    else:
        return None