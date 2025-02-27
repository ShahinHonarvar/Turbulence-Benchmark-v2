def gcf_three_nums(nums):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(gcd(nums[145], nums[183]), nums[770])