def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(nums[46], gcf(nums[84], nums[23]))