def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    return gcf(gcf(nums[76], nums[64]), nums[28])