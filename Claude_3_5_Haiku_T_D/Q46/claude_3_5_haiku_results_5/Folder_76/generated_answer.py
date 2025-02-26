def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcd_three_nums(x, y, z):
        return gcd(gcd(x, y), z)
    return find_gcd_three_nums(nums[876], nums[203], nums[100])