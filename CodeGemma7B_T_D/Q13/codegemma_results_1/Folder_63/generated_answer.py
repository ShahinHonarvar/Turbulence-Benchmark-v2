def find_second_largest_num(nums):
    nums = nums[22:89]
    if not nums:
        return None
    nums.sort()
    return nums[-2]