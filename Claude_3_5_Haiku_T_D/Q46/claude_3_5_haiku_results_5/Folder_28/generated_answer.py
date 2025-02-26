def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def triple_gcf(a, b, c):
        return gcf(gcf(a, b), c)
    return triple_gcf(nums[99], nums[63], nums[74])