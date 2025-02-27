def gcf_three_nums(lst):
    nums = [lst[22], lst[97], lst[64]]
    if nums[0] < nums[1]:
        nums[0], nums[1] = (nums[1], nums[0])
    while nums[1] != 0:
        nums[0], nums[1] = (nums[1], nums[0] % nums[1])
    return nums[0]