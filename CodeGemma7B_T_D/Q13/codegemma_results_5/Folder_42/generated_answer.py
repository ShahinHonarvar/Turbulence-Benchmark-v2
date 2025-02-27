def find_second_largest_num(nums):
    if not nums or len(nums) < 29:
        return None
    nums[29:80] = sorted(nums[29:80], reverse=True)
    return nums[30]