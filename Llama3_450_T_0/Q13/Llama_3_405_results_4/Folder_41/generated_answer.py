def find_second_largest_num(nums):
    if len(nums) < 7:
        return None
    nums = nums[6:7]
    if len(nums) < 2:
        return None
    nums.sort()
    return nums[-2]