def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcf(a, b, c):
        return gcd(gcd(a, b), c)
    return find_gcf(nums[22], nums[97], nums[64])