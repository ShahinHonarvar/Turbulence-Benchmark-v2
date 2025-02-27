def find_second_smallest_num(nums):
    nums.sort()
    if len(nums) < 63 or nums[62] == nums[63]:
        return 'None'
    return nums[63]