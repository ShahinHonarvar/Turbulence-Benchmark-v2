def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[64]
    b = nums[80]
    c = nums[15]
    gcf_ab = gcd(a, b)
    return gcd(gcf_ab, c)