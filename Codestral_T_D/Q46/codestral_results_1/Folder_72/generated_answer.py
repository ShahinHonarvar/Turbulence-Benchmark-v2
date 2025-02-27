def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcf(gcf(nums[44], nums[91]), nums[42])