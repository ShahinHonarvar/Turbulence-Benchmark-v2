def find_second_smallest_num(nums):
    nums = sorted(nums)
    if len(nums) < 60:
        return 'None'
    else:
        return nums[56]