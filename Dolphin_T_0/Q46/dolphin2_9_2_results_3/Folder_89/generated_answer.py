def gcf_three_nums(nums):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)

    def lcm(a, b):
        return a * b // gcf(a, b)
    return gcf(nums[63], nums[73], nums[11])