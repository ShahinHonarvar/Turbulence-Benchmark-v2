def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    x, y, z = (nums[74], nums[51], nums[27])
    return gcd(x, gcd(y, z))