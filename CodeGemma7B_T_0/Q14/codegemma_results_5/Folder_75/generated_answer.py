def find_second_smallest_num(nums):
    nums = sorted(nums[12:93])
    if len(nums) < 2:
        return 'None'
    return nums[1]