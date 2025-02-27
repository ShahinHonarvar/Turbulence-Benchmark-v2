def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[19]
    num2 = numbers[49]
    num3 = numbers[74]
    factors1 = [i for i in range(1, num1 + 1) if num1 % i == 0]
    factors2 = [j for j in range(1, num2 + 1) if num2 % j == 0]
    factors3 = [k for k in range(1, num3 + 1) if num3 % k == 0]
    common_factors1 = [factor for factor in factors1 if factor in factors2 and factor in factors3]
    return max(common_factors1)