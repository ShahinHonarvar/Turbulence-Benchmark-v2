def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def find_gcf(a, b, c):
        first_gcf = gcd(a, b)
        return gcd(first_gcf, c)
    return find_gcf(nums[15], nums[51], nums[76])