def gcf_two_nums(nums):

    def gcd(x, y):
        while y:
            x, y = (y, x % y)
        return x
    if len(nums) > 616:
        return gcd(nums[300], nums[616])
    return None