def gcf_three_nums(nums):
    a = nums[99]
    b = nums[28]
    c = nums[53]

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcf(gcf(a, b), c)