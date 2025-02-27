def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(nums[0], gcf(nums[3], nums[8]))