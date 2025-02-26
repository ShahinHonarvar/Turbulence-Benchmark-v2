def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_three(a, b, c):
        return gcf(gcf(a, b), c)
    return gcf_three(nums[19], nums[69], nums[97])