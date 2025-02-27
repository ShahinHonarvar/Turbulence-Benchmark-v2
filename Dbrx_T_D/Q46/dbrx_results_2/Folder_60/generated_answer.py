def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num96, num53, num35 = (nums[96], nums[53], nums[35])
    return gcd(num96, gcd(num53, num35))