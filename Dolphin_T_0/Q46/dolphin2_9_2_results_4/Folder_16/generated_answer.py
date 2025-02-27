def gcf_three_nums(nums):
    a = nums[558]
    b = nums[110]
    c = nums[628]

    def gcf(a, b):
        if b == 0:
            return a
        return gcf(b, a % b)
    return gcf(gcf(a, b), c)