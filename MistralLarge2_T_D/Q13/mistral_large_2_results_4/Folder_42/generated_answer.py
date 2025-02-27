def find_second_largest_num(nums):
    if len(nums) < 80:
        return None
    sublist = nums[29:80]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]