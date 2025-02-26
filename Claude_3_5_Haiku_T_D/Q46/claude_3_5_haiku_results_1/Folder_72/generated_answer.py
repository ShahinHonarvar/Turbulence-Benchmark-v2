def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_multiple(a, b, c):
        first_gcf = gcd(a, b)
        return gcd(first_gcf, c)
    return gcf_multiple(nums[44], nums[91], nums[42])