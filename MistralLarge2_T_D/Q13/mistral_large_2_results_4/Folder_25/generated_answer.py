def find_second_largest_num(nums):
    if not nums or len(nums) < 94:
        return None
    sublist = nums[29:94]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]