def find_second_largest_num(nums):
    if not nums or len(nums) < 2:
        return None
    nums = nums[56:83]
    max_num = max(nums)
    nums.remove(max_num)
    if not nums:
        return None
    return max(nums)