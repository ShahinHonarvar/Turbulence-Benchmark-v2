def gcf_three_nums(nums):
    gcf = nums[34]
    nums_2 = nums[38]
    nums_3 = nums[77]
    i = gcf
    while i > 1:
        if nums_2 % i == 0 and nums_3 % i == 0:
            return i
        i -= 1
    return 1