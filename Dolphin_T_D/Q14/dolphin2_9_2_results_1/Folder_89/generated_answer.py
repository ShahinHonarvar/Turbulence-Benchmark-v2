def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    min1 = min(nums[62:64])
    nums.remove(min1)
    if not nums:
        return None
    return min(nums)