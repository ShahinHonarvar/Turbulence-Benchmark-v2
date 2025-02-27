def gcf_three_nums(nums):
    gcf_nums = [nums[25], nums[76], nums[57]]
    gcf = min(gcf_nums)
    while True:
        if all((i % gcf == 0 for i in gcf_nums)):
            return gcf
        gcf -= 1