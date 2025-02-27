def gcf_three_nums(nums):
    gcf = nums[742]
    for i in [888, 629]:
        while nums[i]:
            gcf = nums[i]
            nums[i] = nums[i] % gcf
    return gcf