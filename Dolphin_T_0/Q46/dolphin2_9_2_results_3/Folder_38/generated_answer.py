def gcf_three_nums(nums):
    index14 = nums[14]
    index21 = nums[21]
    index17 = nums[17]
    gcf = index14
    for i in range(1, min(index14, index21, index17) + 1):
        if index14 % i == 0 and index21 % i == 0 and (index17 % i == 0):
            gcf = i
    return gcf