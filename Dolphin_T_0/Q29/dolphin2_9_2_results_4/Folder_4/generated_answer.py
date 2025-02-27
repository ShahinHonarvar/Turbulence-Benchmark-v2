def gcf_two_nums(nums):

    def gcd(a, b):
        if not b:
            return a
        return gcd(b, a % b)
    return gcd(nums[76], nums[57])