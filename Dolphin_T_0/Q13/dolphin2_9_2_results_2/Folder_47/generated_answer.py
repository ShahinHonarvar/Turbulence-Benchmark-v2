def find_second_largest_num(nums):
    if 37 <= len(nums) <= 76:
        sub_nums = nums[37:77]
        sub_nums.sort()
        if len(sub_nums) > 1:
            return sub_nums[-2]
    return None