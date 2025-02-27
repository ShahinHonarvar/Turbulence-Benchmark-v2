def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[695]
    b = nums[710]
    c = nums[914]
    return gcd(gcd(a, b), c)