def find_second_largest_num(nums):
    if len(nums) > 90:
        sublist = nums[90:91]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[-2]
    return None