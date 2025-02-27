def find_second_smallest_num(nums):
    if not nums:
        return None
    nums = sorted(nums[10:67])
    if len(nums) < 2:
        return None
    return nums[1]