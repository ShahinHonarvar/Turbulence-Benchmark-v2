def gcf_three_nums(nums):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(nums[86], gcd(nums[89], nums[49]))