def gcf_three_nums(nums):
    a = nums[9]
    b = nums[6]
    c = nums[2]

    def gcd(a, b):
        if b == 0:
            return a
        else:
            return gcd(b, a % b)
    common_factor = gcd(gcd(a, b), c)
    return common_factor