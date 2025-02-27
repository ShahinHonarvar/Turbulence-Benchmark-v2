def gcf_two_nums(nums):

    def calculate_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return calculate_gcf(nums[19], nums[94])