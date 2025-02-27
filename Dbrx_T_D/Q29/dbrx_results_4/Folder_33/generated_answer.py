import functools

def gcf_two_nums(nums):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = nums[166]
    num2 = nums[106]
    common_factors = []
    for i in range(1, num1 + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_factors.append(i)
    return functools.reduce(gcd, common_factors)