def gcf_three_nums(nums):

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(nums[4], gcf(nums[0], nums[8]))