def find_second_largest_num(nums):
    if len(nums) != 0:
        nums = nums[62:93]
        if len(nums) > 1:
            sorted_nums = sorted(nums, reverse=True)
            return sorted_nums[1]
    return None