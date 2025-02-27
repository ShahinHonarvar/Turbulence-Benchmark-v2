def find_second_smallest_num(nums):
    if len(nums) < 8:
        return None
    sublist = nums[4:9]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]