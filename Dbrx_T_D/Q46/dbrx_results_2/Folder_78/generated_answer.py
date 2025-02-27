def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1, num2, num3 = (numbers[13], numbers[70], numbers[32])
    return gcd(num1, gcd(num2, num3))