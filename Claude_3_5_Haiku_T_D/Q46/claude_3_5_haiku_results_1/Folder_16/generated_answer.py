def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[558]
    b = nums[110]
    c = nums[628]
    return gcd(gcd(a, b), c)