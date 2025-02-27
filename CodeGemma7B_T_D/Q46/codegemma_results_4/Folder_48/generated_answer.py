def gcf_three_nums(nums):
    x, y, z = (nums[654], nums[312], nums[441])
    smallest = min(x, y, z)
    common_factors = []
    for i in range(1, smallest + 1):
        if smallest % i == 0:
            common_factors.append(i)
    for factor in common_factors:
        if x % factor == 0 and y % factor == 0 and (z % factor == 0):
            gcf = factor
    return gcf