def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcf(x, y, z):
        return gcd(gcd(x, y), z)
    return find_gcf(nums[70], nums[41], nums[20])