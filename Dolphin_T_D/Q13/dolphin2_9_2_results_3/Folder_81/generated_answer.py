def find_second_largest_num(nums):
    if len(nums) == 0 or len(nums) < 100:
        return None
    nums = nums[10:101]
    max_num = max(nums)
    nums.remove(max_num)
    if len(nums) == 0:
        return None
    second_max_num = max(nums)
    return second_max_num