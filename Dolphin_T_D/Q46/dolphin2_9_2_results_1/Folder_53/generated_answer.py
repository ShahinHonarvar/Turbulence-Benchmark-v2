def gcf_three_nums(nums):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(gcd(nums[66], nums[56]), nums[92])