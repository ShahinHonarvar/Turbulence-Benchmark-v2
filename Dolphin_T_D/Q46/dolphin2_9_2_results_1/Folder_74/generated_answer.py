def gcf_three_nums(nums):
    a = nums[99]
    b = nums[95]
    c = nums[80]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(a, b), c)