def find_second_largest_num(nums):
    sub_nums = nums[6:9]
    if len(sub_nums) < 2:
        return None
    else:
        return sorted(sub_nums)[-2]