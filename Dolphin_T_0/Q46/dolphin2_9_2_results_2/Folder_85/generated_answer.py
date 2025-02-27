def gcf_three_nums(nums):
    a = nums[49]
    b = nums[46]
    c = nums[13]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def gcf(a, b, c):
        return gcd(a, gcd(b, c))
    return gcf(a, b, c)