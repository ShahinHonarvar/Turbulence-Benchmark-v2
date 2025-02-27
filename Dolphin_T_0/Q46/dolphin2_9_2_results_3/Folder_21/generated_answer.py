def gcf_three_nums(nums):
    a = nums[412]
    b = nums[932]
    c = nums[337]

    def gcf(a, b):
        while b:
            a, b = (b, a % b)
        return a
    g = gcf(a, b)

    def gcf(g, c):
        while c:
            g, c = (c, g % c)
        return g
    return g