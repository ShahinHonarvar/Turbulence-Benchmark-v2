def gcf_three_nums(nums):
    a = nums[35]
    b = nums[76]
    c = nums[74]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(gcd(a, b), c)