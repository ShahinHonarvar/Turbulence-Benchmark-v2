def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_of_three(x, y, z):
        first_two_gcf = gcd(x, y)
        return gcd(first_two_gcf, z)
    return gcf_of_three(nums[21], nums[51], nums[33])