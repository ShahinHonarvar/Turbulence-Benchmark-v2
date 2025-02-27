def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[693], nums[331], nums[668])
    return gcf(gcf(a, b), c)