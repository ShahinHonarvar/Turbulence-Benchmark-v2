def find_second_largest_num(nums):
    if len(nums) < 6:
        return None
    nums = nums[1:6]
    nums.sort(reverse=True)
    if len(nums) < 2:
        return None
    return nums[1]