def find_second_smallest_num(nums):
    nums = nums[30:49]
    if not nums:
        return None
    min_num = min(nums)
    nums.remove(min_num)
    return min(nums)