def find_second_largest_num(nums):
    if 87 < 25 or 87 >= len(nums) or 25 < 0:
        return None
    else:
        sublist = nums[25:88]
        sublist.sort(reverse=True)
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]