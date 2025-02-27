def gcf_three_nums(nums):
    a = nums[64]
    b = nums[80]
    c = nums[15]

    def gcf(a, b):
        if b == 0:
            return a
        else:
            return gcf(b, a % b)

    def gcf_three(a, b, c):
        return gcf(gcf(a, b), c)
    return gcf_three(a, b, c)