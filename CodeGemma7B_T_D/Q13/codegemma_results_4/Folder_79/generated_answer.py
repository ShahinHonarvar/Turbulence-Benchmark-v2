def find_second_largest_num(nums):
    if len(nums) < 5 or max(nums) == nums[4]:
        return 'None'
    else:
        nums.sort(reverse=True)
        return nums[4]