def gcf_two_nums(nums):

    def _gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return _gcf(nums[0], nums[1])