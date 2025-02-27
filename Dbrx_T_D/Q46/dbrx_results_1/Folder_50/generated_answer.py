def gcf_three_nums(nums):
    a = nums[20]
    b = nums[35]
    c = nums[74]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    return gcd(lcm(a, b), c)