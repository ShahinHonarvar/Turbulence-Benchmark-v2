def find_second_smallest_num(nums):
    if len(nums) < 59 or 25 >= len(nums):
        return None
    sublist = nums[25:60]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]