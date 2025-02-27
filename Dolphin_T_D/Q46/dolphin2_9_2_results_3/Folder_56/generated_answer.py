def gcf_three_nums(nums):

    def gcf(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    return gcf(nums[59], gcf(nums[93], nums[84]))