def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(nums[74], nums[60]), nums[28])