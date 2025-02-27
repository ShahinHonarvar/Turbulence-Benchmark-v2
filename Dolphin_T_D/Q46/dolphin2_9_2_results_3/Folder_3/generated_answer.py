def gcf_three_nums(numbers):
    num1 = numbers[31]
    num2 = numbers[69]
    num3 = numbers[40]

    def gcd(a, b):
        while b > 0:
            a, b = (b, a % b)
        return a
    gcf = gcd(gcd(num1, num2), num3)
    return gcf