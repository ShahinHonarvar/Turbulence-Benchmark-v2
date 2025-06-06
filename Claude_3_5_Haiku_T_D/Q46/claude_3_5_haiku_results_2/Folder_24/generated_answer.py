def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcf(a, b, c):
        return gcd(gcd(a, b), c)
    return find_gcf(nums[18], nums[37], nums[43])