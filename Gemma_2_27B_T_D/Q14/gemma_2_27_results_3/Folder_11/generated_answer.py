def find_second_smallest_num(nums):
    if len(nums) < 94:
        return None
    sublist = nums[66:94]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]