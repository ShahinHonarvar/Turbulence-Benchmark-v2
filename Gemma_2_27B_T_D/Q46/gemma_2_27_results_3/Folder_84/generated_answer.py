def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(nums[695], nums[710]), nums[914])