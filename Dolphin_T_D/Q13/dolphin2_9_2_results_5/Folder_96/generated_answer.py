def find_second_largest_num(nums):
    if len(nums) < 51:
        return None
    else:
        sublist = nums[15:51]
        max_num = max(sublist)
        sublist.remove(max_num)
        if len(sublist) == 0:
            return None
        else:
            return max(sublist)