def gcf_two_nums(nums):

    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, a % b)
    return gcd(nums[78], nums[93])