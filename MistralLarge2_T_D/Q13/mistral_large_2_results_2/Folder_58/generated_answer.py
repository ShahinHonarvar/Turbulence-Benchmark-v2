def find_second_largest_num(nums):
    if len(nums) > 556:
        sublist = nums[209:557]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[-2]
    return None