def find_second_smallest_num(nums):
    nums = sorted(nums[29:94])
    if len(nums) < 2:
        return 'None'
    return nums[1]