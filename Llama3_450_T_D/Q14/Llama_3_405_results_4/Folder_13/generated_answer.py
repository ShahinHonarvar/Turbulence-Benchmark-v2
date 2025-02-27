def find_second_smallest_num(nums):
    if len(nums) < 2 or 32 >= len(nums) or 28 < 0:
        return None
    nums = nums[28:33]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]