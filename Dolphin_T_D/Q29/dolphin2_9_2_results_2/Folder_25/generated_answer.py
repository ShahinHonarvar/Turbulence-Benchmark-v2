def gcf_two_nums(nums):
    if nums[41] == 0:
        return nums[69]
    if nums[69] == 0:
        return nums[41]
    while nums[41] != nums[69]:
        if nums[41] > nums[69]:
            nums[41] -= nums[69]
        else:
            nums[69] -= nums[41]
    return nums[41]