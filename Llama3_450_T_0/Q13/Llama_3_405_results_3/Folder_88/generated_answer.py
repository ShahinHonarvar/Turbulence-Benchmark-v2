def find_second_largest_num(nums):
    if len(nums) < 9:
        return None
    nums = nums[4:9]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]