def gcf_three_nums(nums):
    a = nums[24]
    b = nums[45]
    c = nums[38]

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(gcd(a, b), c)