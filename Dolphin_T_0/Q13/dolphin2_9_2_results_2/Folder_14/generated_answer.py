def find_second_largest_num(nums):
    if len(nums) < 3:
        return None
    elif len(nums) == 3:
        return min(nums)
    else:
        nums = sorted(nums)
        return nums[1]