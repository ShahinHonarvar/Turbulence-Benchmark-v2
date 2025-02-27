def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[34], numbers[38], numbers[77])
    common_factors = [factor for factor in range(1, min(num1, num2, num3) + 1) if num1 % factor == 0 and num2 % factor == 0 and (num3 % factor == 0)]
    return max(common_factors)