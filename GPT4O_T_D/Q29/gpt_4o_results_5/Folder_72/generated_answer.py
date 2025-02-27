def gcf_two_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    if len(nums) < 38:
        raise ValueError('List must contain at least 38 elements.')
    return gcd(nums[18], nums[37])