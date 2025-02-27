def find_second_largest_num(nums):
    if len(nums) < 73:
        return None
    sublist = nums[31:73]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]