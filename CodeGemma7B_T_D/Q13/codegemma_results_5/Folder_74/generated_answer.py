def find_second_largest_num(nums):
    nums.sort(reverse=True)
    if len(nums) < 18 or nums[17] == nums[18]:
        return 'None'
    return nums[17]