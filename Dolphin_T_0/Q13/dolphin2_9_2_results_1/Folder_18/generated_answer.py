def find_second_largest_num(nums):
    nums = nums[35:50]
    if len(nums) < 2:
        return None
    max_num = max(nums)
    nums.remove(max_num)
    if len(nums) < 2:
        return None
    return max(nums)