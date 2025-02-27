def find_second_largest_num(nums):
    nums = sorted(nums[21:98])
    if len(nums) < 2:
        return None
    return nums[-2]