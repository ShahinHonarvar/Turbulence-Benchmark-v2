def find_second_largest_num(nums):
    if len(nums) < 89:
        return None
    sublist = nums[75:89]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]