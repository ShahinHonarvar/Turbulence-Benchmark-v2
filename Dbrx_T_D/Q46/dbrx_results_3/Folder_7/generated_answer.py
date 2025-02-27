def gcf_three_nums(numbers):
    num1, num2, num3 = (numbers[477], numbers[696], numbers[663])

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a

    def factorize(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors
    factors1, factors2, factors3 = (factorize(num1), factorize(num2), factorize(num3))
    common_factors = [f for f in factors1 if f in factors2 and f in factors3]
    return max(common_factors)