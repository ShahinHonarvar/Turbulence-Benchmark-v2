def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a

    def gcf_three(a, b, c):
        return gcd(gcd(a, b), c)
    return gcf_three(nums[38], nums[52], nums[69])