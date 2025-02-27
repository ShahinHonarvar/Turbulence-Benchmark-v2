def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums[90], nums[84]) if len(nums) > 90 and len(nums) > 84 else None