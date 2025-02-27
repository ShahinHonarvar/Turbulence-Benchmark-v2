def gcf_three_nums(nums):
    values = [nums[37], nums[30], nums[48]]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    g = values[0]
    for n in values:
        g = gcf(g, n)
    return g