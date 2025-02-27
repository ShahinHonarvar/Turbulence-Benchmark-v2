def gcf_three_nums(nums):
    a = nums[90]
    b = nums[54]
    c = nums[96]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(gcd(a, b), c)