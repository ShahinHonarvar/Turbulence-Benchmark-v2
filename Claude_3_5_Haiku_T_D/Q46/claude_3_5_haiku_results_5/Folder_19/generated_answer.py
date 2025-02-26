def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[40]
    num2 = numbers[15]
    num3 = numbers[99]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf