def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(nums[16], gcf(nums[87], nums[95]))