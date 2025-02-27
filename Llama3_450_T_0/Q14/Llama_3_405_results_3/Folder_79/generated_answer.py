def find_second_smallest_num(nums):
    if len(nums) < 6:
        return None
    nums = sorted(nums[1:6])
    if len(nums) < 2:
        return None
    return nums[1]