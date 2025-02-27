def gcf_two_nums(nums):
    while nums[0] != nums[9]:
        if nums[0] > nums[9]:
            nums[0] = nums[0] - nums[9]
        else:
            nums[9] = nums[9] - nums[0]
    return nums[0]