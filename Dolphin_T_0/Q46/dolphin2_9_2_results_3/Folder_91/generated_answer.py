def gcf_three_nums(nums):

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)
    return gcf(gcf(nums[8], nums[9]), nums[3])