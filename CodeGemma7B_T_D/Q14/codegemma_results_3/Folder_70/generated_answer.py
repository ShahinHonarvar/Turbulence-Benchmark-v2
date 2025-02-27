def find_second_smallest_num(nums):
    nums = nums[35:50]
    nums.sort()
    if len(nums) < 2:
        return 'None'
    else:
        return nums[1]