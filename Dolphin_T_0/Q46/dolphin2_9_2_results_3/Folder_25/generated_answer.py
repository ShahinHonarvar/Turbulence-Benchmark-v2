def gcf_three_nums(nums):

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    return gcd(nums[32], gcd(nums[54], nums[13]))