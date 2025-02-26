def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[37]
    b = nums[30]
    c = nums[48]
    return gcd(gcd(a, b), c)