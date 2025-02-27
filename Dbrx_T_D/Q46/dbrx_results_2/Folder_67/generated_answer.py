def gcf_three_nums(numbers):

    def gcd(a, b):
        return gcd(b, a % b) if b else abs(a)
    num1 = numbers[70]
    num2 = numbers[41]
    num3 = numbers[20]
    factors = [factor for factor in range(1, min(num1, num2, num3) + 1) if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0)]
    return max(factors)