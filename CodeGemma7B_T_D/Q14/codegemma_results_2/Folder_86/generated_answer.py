def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 37 or 33 not in range(len(nums)) or 36 not in range(len(nums)):
        return 'None'
    return nums[33] if nums[33] == nums[34] else nums[34]