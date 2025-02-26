def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_of_three(x, y, z):
        return gcd(gcd(x, y), z)
    return gcf_of_three(nums[93], nums[94], nums[57])