def find_second_smallest_num(nums):
    if len(nums) < 2 or 8 < len(nums):
        return None
    nums = sorted(nums[1:9])
    if len(nums) < 2:
        return None
    return nums[1]