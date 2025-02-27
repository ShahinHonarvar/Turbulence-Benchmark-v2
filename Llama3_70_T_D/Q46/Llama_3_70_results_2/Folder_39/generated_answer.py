def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a, b, c = (nums[85], nums[36], nums[54])
    gcf = gcd(gcd(a, b), c)
    return gcf