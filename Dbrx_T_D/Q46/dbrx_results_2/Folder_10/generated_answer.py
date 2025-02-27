def gcf_three_nums(nums):
    a = nums[86]
    b = nums[89]
    c = nums[49]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(a, b), c)