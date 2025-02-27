def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[13], nums[76], nums[44])
    return gcd(gcd(a, b), c)