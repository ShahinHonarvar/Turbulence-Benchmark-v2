def gcf_two_nums(nums):

    def _gcd(x, y):
        if y == 0:
            return x
        return _gcd(y, x % y)
    return _gcd(nums[33], nums[72])