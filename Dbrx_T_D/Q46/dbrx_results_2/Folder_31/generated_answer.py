def gcf_three_nums(numbers):
    num1 = numbers[90]
    num2 = numbers[54]
    num3 = numbers[96]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return abs(a)
    factor = gcd(gcd(num1, num2), num3)
    return factor