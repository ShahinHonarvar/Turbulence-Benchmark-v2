def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_multiple(x, y, z):
        first_gcf = gcd(x, y)
        return gcd(first_gcf, z)
    return gcf_multiple(nums[990], nums[671], nums[711])