def gcf_three_nums(nums):

    def gcf(a, b):
        if not b:
            return a
        return gcf(b, a % b)
    return gcf(nums[4], gcf(nums[1], nums[7]))