def find_second_smallest_num(nums):
    if len(nums) < 28 or len(nums) > 32:
        return 'None'
    nums[28:32].sort()
    return nums[29]