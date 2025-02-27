def gcf_three_nums(nums):

    def _gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[99]
    b = nums[28]
    c = nums[53]
    gcf = a
    for i in [b, c]:
        gcf = _gcf(gcf, i)
    return gcf