def gcf_three_nums(lst):

    def gcf(a, b):
        if a == 0:
            return b
        return gcf(b % a, a)
    nums = [lst[14], lst[21], lst[17]]
    g = nums[0]
    for n in nums[1:]:
        g = gcf(g, n)
    return g