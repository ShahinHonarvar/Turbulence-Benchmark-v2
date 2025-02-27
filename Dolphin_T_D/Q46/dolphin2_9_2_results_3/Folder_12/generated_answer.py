def gcf_three_nums(nums):
    a = nums[91]
    b = nums[45]
    c = nums[48]

    def gcd(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    if a <= 0 or b <= 0 or c <= 0:
        return None
    return gcd(gcd(a, b), c)