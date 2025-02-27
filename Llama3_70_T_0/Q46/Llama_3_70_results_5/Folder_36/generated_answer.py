def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[427]
    b = nums[761]
    c = nums[148]
    return gcd(gcd(a, b), c)