def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) <= 85 or nums[85] == nums[-2]:
        return None
    return nums[85]