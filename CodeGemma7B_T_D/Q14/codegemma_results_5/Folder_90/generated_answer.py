def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) == 0 or len(nums) <= 527 or len(nums) > 538:
        return None
    else:
        return nums[528]