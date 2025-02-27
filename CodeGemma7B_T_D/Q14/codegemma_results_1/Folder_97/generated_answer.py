def find_second_smallest_num(nums):
    if len(nums) < 5 or max(nums) >= 35 or min(nums) <= 30:
        return 'None'
    nums = sorted(nums[30:35])
    if len(nums) == 0:
        return 'None'
    elif len(nums) == 1:
        return nums[0]
    else:
        return nums[1]