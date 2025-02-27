def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(nums[252], nums[149])
    gcf = gcd(gcf, nums[564])
    return gcf