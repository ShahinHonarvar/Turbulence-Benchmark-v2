def find_second_smallest_num(nums):
    if len(nums) < 3:
        return None
    sublist = nums[1:9]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]