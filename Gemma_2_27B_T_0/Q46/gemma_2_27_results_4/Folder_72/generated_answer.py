def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(nums[44], gcf(nums[91], nums[42]))