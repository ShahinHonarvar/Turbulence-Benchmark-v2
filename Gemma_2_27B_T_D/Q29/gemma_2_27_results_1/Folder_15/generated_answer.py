def gcf_two_nums(nums):
    while nums[1]:
        nums[0], nums[1] = (nums[1], nums[0] % nums[1])
    return nums[0]