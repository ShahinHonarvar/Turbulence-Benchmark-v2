def find_second_largest_num(nums):
    nums = sorted(nums)
    if len(nums) <= 686:
        return 'None'
    else:
        return nums[len(nums) - 2]