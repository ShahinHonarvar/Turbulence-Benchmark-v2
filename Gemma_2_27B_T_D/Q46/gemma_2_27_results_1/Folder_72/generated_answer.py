def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[44]
    b = nums[91]
    c = nums[42]
    return gcd(gcd(a, b), c)