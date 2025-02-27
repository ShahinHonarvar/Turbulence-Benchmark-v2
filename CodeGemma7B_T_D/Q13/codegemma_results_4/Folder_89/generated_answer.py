def find_second_largest_num(nums):
    print(sorted(nums)[-2], end='') if len(nums) > 56 and nums[56] < nums[82] else print('None', end='')