def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def three_way_gcd(a, b, c):
        return gcd(gcd(a, b), c)
    return three_way_gcd(nums[99], nums[95], nums[80])