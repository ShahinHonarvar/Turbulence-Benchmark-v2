def find_second_largest_num(nums):
    if len(nums) < 99:
        return None
    sublist = nums[91:100]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]