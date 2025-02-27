def find_second_largest_num(nums):
    nums = nums[667:775]
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return None
    max_num = max(nums)
    nums.remove(max_num)
    if len(nums) == 0:
        return None
    second_max_num = max(nums)
    return second_max_num