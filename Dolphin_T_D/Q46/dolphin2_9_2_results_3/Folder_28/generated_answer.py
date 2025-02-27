def gcf_three_nums(nums):
    a = nums[99]
    b = nums[63]
    c = nums[74]

    def gcf(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    g = gcf(a, b)
    result = gcf(g, c)
    return result