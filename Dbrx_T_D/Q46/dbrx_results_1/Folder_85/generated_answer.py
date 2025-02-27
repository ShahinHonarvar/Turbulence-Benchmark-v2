def gcf_three_nums(nums):

    def gcf(x, y):
        while y != 0:
            x, y = (y, x % y)
        return x
    a = nums[49]
    b = nums[46]
    c = nums[13]
    return gcf(gcf(a, b), c)