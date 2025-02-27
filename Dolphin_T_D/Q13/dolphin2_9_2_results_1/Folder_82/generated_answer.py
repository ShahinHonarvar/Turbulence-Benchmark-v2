def find_second_largest_num(nums):
    new_nums = nums[20:201]
    if len(new_nums) < 2:
        return None
    else:
        return sorted(new_nums)[-2]