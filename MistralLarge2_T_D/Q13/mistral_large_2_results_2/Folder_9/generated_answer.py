def find_second_largest_num(nums):
    if len(nums) > 200:
        sublist = nums[200:201]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[-2]
    return None