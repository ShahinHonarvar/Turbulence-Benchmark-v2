def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 247 or len(nums) > 751:
        return 'None'
    else:
        return nums[246:751][1]