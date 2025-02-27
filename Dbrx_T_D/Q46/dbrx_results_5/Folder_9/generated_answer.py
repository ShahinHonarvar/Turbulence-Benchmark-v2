def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def factor_finder(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def gcf_three_nums(nums):
    a, b, c = (nums[66 - 1], nums[90 - 1], nums[27 - 1])
    factors_a = factor_finder(a)
    factors_b = factor_finder(b)
    factors_c = factor_finder(c)
    common_factors = [val for val in factors_a if val in factors_b and val in factors_c]
    return max(common_factors)