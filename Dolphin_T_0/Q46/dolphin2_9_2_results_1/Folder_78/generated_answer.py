def gcf_three_nums(nums):
    a = nums[13]
    b = nums[70]
    c = nums[32]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def gcf(a, b, c):
        if b == 0:
            return gcd(a, c)
        else:
            return gcd(a, gcf(b, c))
    return gcf(a, b, c)