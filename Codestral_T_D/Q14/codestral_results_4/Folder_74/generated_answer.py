def find_second_smallest_num(nums):
    if len(nums) >= 47:
        sublist = nums[36:47]
        sublist.sort()
        return sublist[1] if len(sublist) > 1 else None
    else:
        return None