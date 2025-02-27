def gcf_three_nums(nums):

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[70], nums[98], nums[22])
    return gcf(gcf(a, b), c)