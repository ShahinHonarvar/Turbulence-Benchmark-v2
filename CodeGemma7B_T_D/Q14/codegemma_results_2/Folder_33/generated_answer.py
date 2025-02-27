def find_second_smallest_num(nums):
    if not nums:
        return None
    nums = sorted(nums)
    for num in nums[262:747]:
        if len(nums) > 2:
            return nums[2]
    if len(nums) == 2:
        return nums[1]
    return None