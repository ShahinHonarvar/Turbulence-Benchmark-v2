def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    if len(nums) < 67:
        raise ValueError('Input list must have at least 67 elements')
    return gcd(nums[13], nums[66])