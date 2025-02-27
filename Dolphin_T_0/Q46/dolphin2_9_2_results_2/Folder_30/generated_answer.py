def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    return gcd(nums[76], gcd(nums[35], nums[74]))