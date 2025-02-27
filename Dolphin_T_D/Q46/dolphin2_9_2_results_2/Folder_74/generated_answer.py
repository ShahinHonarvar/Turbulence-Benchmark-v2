def gcf_three_nums(nums):

    def gcf(x, y):
        while y:
            x, y = (y, x % y)
        return x
    a = nums[99]
    b = nums[95]
    c = nums[80]
    gcf_ab = gcf(a, b)
    gcf_abc = gcf(gcf_ab, c)
    return gcf_abc