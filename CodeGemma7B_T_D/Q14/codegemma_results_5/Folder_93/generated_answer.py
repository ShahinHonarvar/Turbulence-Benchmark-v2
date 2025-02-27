def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) >= 88:
        return nums[75]
    else:
        return 'None'