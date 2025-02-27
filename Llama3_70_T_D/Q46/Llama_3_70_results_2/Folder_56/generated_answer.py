def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a = nums[59]
    b = nums[93]
    c = nums[84]
    gcf_ab = gcd(a, b)
    return gcd(gcf_ab, c)