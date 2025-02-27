def find_second_largest_num(nums):
    if not nums:
        return None
    nums = nums[25:88]
    nums.sort()
    return nums[-2] if len(nums) >= 2 else None