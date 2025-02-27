def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[4]
    num2 = numbers[0]
    num3 = numbers[8]
    factor1 = gcd(num1, num2)
    factor2 = gcd(factor1, num3)
    return factor2