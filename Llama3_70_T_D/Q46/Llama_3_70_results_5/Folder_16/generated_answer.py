def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    gcf_558_110 = gcf(nums[558], nums[110])
    return gcf(gcf_558_110, nums[628])