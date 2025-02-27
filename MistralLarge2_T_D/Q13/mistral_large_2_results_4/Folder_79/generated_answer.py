def find_second_largest_num(nums):
    if len(nums) > 4:
        sublist = nums[4:5]
        if len(sublist) > 1:
            return sorted(sublist)[-2]
    return None