def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    n1, n2 = (nums[36], nums[54])
    return gcd(n1, n2) if n1 <= n2 else gcd(n2, n1)