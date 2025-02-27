def find_second_largest_num(nums):
    if len(nums[56:67]) < 2:
        return None
    nums = nums[56:67]
    max_n = max(nums)
    nums.remove(max_n)
    if len(nums) == 1:
        return None
    return max(nums)