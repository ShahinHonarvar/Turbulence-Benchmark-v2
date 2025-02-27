def find_second_smallest_num(nums):
    if len(nums) < 22 or 95 >= len(nums):
        return None
    sublist = nums[74:96]
    sublist.sort()
    return sublist[1]