def gcf_three_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    n1, n2, n3 = (nums[85], nums[36], nums[54])
    return gcd(n1, gcd(n2, n3))