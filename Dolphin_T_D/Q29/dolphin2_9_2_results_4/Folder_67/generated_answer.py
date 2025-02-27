def gcf_two_nums(nums):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(nums[64], nums[28])