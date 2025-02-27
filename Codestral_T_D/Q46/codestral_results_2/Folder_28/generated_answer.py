def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[99]
    num2 = numbers[63]
    num3 = numbers[74]
    return gcd(gcd(num1, num2), num3)