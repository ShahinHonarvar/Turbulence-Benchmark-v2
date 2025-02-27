def find_second_smallest_num(nums):
    if not nums or len(nums) < 23 or max(nums) < 23 or (min(nums) > 50):
        return None
    nums = sorted(nums[22:51])
    if len(nums) < 2:
        return None
    return nums[1]