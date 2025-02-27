def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[25]
    b = nums[76]
    c = nums[57]
    return gcd(gcd(a, b), c)