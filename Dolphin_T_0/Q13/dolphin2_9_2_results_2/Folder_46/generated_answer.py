def find_second_largest_num(nums):
    if not nums:
        return None
    nums = nums[30:88]
    if len(nums) < 2:
        return None
    first = max(nums)
    nums.remove(first)
    second = max(nums)
    return second