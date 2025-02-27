def find_second_smallest_num(nums):
    if len(nums) < 200 or max(nums) < 90 or min(nums) > 200:
        return None
    nums = sorted(nums)
    for i in range(90, 201):
        if nums[i] > nums[i + 1]:
            return nums[i + 1]
    return None