def find_second_smallest_num(nums):
    sub_nums = nums[74:96]
    sub_nums.sort()
    if len(sub_nums) < 2:
        return None
    else:
        return sub_nums[1]