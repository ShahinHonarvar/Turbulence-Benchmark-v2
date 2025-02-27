def find_second_smallest_num(nums):
    if not nums or len(nums) < 55:
        return None
    nums = nums[34:56]
    nums.sort()
    if len(nums) < 2:
        return None
    return nums[1]