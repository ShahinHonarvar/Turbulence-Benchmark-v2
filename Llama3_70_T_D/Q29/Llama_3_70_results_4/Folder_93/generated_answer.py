def gcf_two_nums(nums):

    def _gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return _gcf(nums[78], nums[16])