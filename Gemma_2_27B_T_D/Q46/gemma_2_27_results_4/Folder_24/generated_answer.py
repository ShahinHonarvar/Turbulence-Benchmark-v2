def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums[18], gcd(nums[37], nums[43]))