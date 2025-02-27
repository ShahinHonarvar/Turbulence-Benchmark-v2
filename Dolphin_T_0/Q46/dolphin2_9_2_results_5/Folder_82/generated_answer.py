def gcf_three_nums(nums):
    values = [nums[67], nums[84], nums[13]]
    gcf = min(values)
    while values:
        gcf = min(values)
        values = [num for num in values if num % gcf == 0]
    return gcf