def gcf_two_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return gcf(nums[841], nums[804])