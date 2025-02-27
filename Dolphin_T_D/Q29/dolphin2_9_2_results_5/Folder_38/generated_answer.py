def gcf_two_nums(ls):
    nums = (ls[88], ls[35])
    while nums[1]:
        nums = [nums[0] % nums[1], min(nums[0], nums[1])]
    return nums[0]