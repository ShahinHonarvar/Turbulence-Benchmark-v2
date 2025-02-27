def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    num1, num2, num3 = (numbers[18], numbers[10], numbers[76])
    return gcd(gcd(num1, num2), num3)