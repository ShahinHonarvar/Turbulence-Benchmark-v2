def gcf_three_nums(lst):
    nums = [lst[46], lst[84], lst[23]]
    gcf = nums[0]
    for i in nums:
        gcf = gcf(gcf, i)
    return gcf