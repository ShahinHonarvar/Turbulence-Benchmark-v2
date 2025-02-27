def find_second_largest_num(nums):
    if len(nums) < 10:
        return None
    nums = nums[8:10]
    if len(nums) < 2:
        return None
    return sorted(nums)[-2]