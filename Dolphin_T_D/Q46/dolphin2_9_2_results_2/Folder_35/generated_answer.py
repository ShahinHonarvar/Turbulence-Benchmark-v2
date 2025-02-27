def gcf_three_nums(nums):
    a = nums[742]
    b = nums[888]
    c = nums[629]

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(a, gcd(b, c))