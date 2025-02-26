def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcf(x, y, z):
        first_gcf = gcd(x, y)
        return gcd(first_gcf, z)
    return find_gcf(nums[20], nums[51], nums[62])