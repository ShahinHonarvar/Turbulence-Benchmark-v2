def find_second_smallest_num(nums):
    if len(nums) < 8 or len(nums) > 52:
        return None
    nums = nums[42:52]
    if len(set(nums)) < 2:
        return None
    nums.sort()
    return nums[1]