def find_second_largest_num(nums):
    if len(nums) < 2:
        return None
    nums = nums[0:6]
    nums.sort()
    return nums[1]