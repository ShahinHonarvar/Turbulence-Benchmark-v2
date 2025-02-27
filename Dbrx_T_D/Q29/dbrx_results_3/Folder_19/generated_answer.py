def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)
    num1 = numbers[66]
    num2 = numbers[90]
    factors1 = [factor for factor in range(1, num1 + 1) if num1 % factor == 0]
    factors2 = [factor for factor in range(1, num2 + 1) if num2 % factor == 0]
    common_factors = [factor for factor in factors1 if factor in factors2]
    return max(common_factors) if common_factors else lcm(num1, num2)