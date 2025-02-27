def gcf_three_nums(nums):
    nums = [nums[27], nums[85], nums[51]]
    gcf = nums[0]
    for i in range(1, len(nums)):
        while nums[i]:
            nums[i], gcf = (gcf % nums[i], gcf)
    return gcf