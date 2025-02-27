def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 29 or nums[28] == nums[-1]:
        return 'None'
    return nums[28 + 1]