def gcf_two_nums(nums):

    def gcf(m, n):
        if n == 0:
            return m
        return gcf(n, m % n)
    return gcf(nums[90], nums[54])