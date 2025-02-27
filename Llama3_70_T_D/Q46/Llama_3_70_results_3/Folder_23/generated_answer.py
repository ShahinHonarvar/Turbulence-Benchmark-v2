def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    a = nums[31]
    b = nums[25]
    c = nums[80]
    g = gcd(a, b)
    return gcd(g, c)