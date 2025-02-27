def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    n1, n2, n3 = (nums[41], nums[69], nums[28])
    return gcd(n1, gcd(n2, n3))