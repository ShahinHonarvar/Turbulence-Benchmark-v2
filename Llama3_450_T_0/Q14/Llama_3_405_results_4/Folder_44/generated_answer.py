def find_second_smallest_num(nums):
    if len(nums) < 100:
        return None
    nums = sorted(nums[91:100])
    if len(nums) < 2:
        return None
    return nums[1]