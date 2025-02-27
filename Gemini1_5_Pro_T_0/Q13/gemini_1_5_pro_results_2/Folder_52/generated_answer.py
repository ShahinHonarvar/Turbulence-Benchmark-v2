def find_second_largest_num(nums):
    sub_nums = nums[28:39]
    if len(sub_nums) < 2:
        return None
    else:
        return sorted(sub_nums)[-2]