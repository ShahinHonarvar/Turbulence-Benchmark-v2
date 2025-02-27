def find_second_largest_num(nums):
    if len(nums) <= 68:
        return None
    sublist = nums[42:69]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]