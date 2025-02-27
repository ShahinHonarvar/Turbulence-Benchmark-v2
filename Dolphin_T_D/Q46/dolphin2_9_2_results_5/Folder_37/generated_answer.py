def gcf_three_nums(nums):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(gcf(nums[41], nums[69]), nums[28])