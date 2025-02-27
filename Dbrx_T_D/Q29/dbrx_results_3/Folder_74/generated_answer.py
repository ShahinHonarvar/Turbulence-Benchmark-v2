def gcf_two_nums(numbers):
    num1 = numbers[36]
    num2 = numbers[85]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    def get_factors(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    num1_factors = get_factors(num1)
    num2_factors = get_factors(num2)
    common_factors = [factor for factor in num1_factors if factor in num2_factors]
    greatest_common_factor = max(common_factors)
    return greatest_common_factor