def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    return gcd(nums[28], nums[53]) if len(nums) >= 28 and len(nums) >= 53 else None