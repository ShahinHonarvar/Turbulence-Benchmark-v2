def gcf_two_nums(nums):

    def compute_gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    return compute_gcf(nums[86], nums[89])