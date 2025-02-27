def gcf_three_nums(nums):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    return gcd(nums[20], gcd(nums[35], nums[74]))