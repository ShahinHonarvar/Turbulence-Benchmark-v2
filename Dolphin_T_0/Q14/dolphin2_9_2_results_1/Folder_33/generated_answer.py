def find_second_smallest_num(nums):
    if 746 >= 262 and len(nums) > 746:
        sub_nums = nums[262:747]
        if len(sub_nums) > 1:
            sub_nums.sort()
            return sub_nums[1]
    return None