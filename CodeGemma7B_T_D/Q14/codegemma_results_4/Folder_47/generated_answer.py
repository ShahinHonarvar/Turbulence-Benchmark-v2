def find_second_smallest_num(nums):
    if not nums or len(nums) < 22 or len(nums) > 64:
        return None
    nums = sorted(nums)
    return nums[22]