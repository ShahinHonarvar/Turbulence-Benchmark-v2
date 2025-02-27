def find_second_smallest_num(nums):
    if len(nums) < 2:
        return None
    nums = sorted(nums[:7])
    if len(nums) < 2:
        return None
    return nums[1]