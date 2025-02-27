def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[13]
    num2 = numbers[54]
    num3 = numbers[56]
    factor1 = gcd(num1, num2)
    return gcd(factor1, num3)