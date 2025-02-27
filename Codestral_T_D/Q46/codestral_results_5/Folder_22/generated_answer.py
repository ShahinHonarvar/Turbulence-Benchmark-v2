def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(gcf(nums[27], nums[85]), nums[51])