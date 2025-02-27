def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    gcf = gcd(nums[974], nums[244])
    return gcd(gcf, nums[991])