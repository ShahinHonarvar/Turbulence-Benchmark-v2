def gcf_three_nums(nums):
    prod = 1
    for num in [nums[21], nums[69], nums[41]]:
        prod *= num
    for i in range(2, int(prod ** 0.5) + 1):
        if prod % i == 0:
            gcf = i
            break
    return gcf