def find_second_largest_num(nums):
    if len(nums) < 201:
        return None
    sublist = nums[40:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]