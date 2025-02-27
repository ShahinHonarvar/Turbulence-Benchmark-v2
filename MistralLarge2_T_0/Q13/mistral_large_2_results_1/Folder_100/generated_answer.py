def find_second_largest_num(nums):
    if len(nums) < 69:
        return None
    sublist = nums[42:69]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]