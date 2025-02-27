def gcf_two_nums(nums):

    def gcd(a, b):
        if a == 0:
            return b
        else:
            return gcd(b % a, a)
    return gcd(nums[64], nums[80])