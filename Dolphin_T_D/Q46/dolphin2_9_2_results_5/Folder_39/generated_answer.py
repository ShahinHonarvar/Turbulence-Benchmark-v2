def gcf_three_nums(nums):

    def gcf(a, b):
        if a % b == 0:
            return b
        return gcf(b, a % b)
    return gcf(gcf(nums[85], nums[36]), nums[54])