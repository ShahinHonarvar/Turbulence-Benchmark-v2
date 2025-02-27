def gcf_two_nums(nums):
    a = nums[46]
    b = nums[13]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(a, b)