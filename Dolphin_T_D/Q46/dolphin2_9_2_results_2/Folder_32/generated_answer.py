def gcf_three_nums(nums):
    a = nums[20]
    b = nums[43]
    c = nums[95]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(a, b), c)