def gcf_three_nums(lst):
    nums = (lst[3], lst[8], lst[9])
    gcf = nums[0]
    for num in nums[1:]:
        while gcf % num:
            gcf -= 1
    return gcf