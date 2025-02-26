def gcf_three_nums(nums):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    a = nums[404]
    b = nums[834]
    c = nums[517]
    return gcd(gcd(a, b), c)