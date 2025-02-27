def gcf_three_nums(nums):
    a = nums[37]
    b = nums[30]
    c = nums[48]

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(a, b), c)