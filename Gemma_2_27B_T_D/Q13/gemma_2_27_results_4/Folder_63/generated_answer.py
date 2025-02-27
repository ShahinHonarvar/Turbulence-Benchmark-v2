def find_second_largest_num(nums):
    if len(nums) < 23 or 88 >= len(nums):
        return None
    sub_nums = nums[22:89]
    return sorted(sub_nums)[-2]