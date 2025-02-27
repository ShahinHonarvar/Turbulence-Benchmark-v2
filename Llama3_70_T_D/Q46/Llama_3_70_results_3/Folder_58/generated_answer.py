def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[145]
    num2 = numbers[183]
    num3 = numbers[770]
    gcf12 = gcd(num1, num2)
    gcf = gcd(gcf12, num3)
    return gcf