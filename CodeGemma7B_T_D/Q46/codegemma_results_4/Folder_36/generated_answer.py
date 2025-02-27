def gcf_three_nums(nums):

    def gcd(a, b):
        return b if a == 0 else gcd(b % a, a)
    return gcd(nums[427], gcd(nums[761], nums[148]))