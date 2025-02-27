def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[404]
    num2 = numbers[834]
    num3 = numbers[517]
    factor1 = gcd(num1, num2)
    factor2 = gcd(factor1, num3)
    return factor2