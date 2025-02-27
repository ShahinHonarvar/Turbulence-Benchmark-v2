def find_second_largest_num(nums):
    if 262 <= len(nums) <= 746:
        nums_sub = nums[262:746]
        nums_sort = sorted(nums_sub, reverse=True)
        if len(nums_sort) > 1:
            return nums_sort[1]
    return None