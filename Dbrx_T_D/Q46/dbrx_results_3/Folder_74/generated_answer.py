def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[99], nums[95], nums[80])
    return gcd(a, gcd(b, c))