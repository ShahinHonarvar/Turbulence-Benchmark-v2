def find_second_largest_num(nums):
    if len(nums) <= 200:
        return None
    sublist = nums[100:201]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]