def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[990]
    num2 = numbers[671]
    num3 = numbers[711]
    factor = gcd(num1, gcd(num2, num3))
    return factor