def find_second_smallest_num(nums):
    if len(nums) < 29 or len(nums) > 39:
        return 'None'
    nums.sort()
    return nums[28]