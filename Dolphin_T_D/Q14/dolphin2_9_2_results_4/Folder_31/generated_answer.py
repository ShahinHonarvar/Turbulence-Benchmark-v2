def find_second_smallest_num(nums):
    if not (len(nums) > 93 and len(nums) <= 100):
        return None
    sublist = nums[29:94]
    sublist.sort()
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]