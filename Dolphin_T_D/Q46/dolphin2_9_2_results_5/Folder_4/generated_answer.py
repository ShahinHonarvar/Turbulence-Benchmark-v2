def gcf_three_nums(nums):
    a = nums[24]
    b = nums[25]
    c = nums[80]

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    gcd_ab = gcd(a, b)
    gcd_abc = gcd(gcd_ab, c)
    return gcd_abc