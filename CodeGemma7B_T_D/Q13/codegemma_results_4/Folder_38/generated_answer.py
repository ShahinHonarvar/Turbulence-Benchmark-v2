def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) >= 46:
        return nums[22]
    else:
        return 'None'