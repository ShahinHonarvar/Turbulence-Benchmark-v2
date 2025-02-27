def gcf_three_nums(lst):
    nums = [lst[44], lst[91], lst[42]]
    gcf = nums[0]
    for num in nums:
        gcf = int(gcf * num / abs(gcf * num))
    return gcf