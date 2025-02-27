def gcf_two_nums(nums):
    i = 86
    j = 89
    if len(nums) <= i or len(nums) <= j:
        return -1
    while nums[i] != nums[j]:
        if nums[i] > nums[j]:
            nums[i] = nums[i] - nums[j]
        else:
            nums[j] = nums[j] - nums[i]
    return nums[i]