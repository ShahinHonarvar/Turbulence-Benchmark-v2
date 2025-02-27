def gcf_three_nums(nums):

    def gcf(a, b):
        while b != 0:
            a %= b
            if a == 0:
                b = a
            else:
                a = b
        return a
    return gcf(gcf(nums[64], nums[80]), nums[15])