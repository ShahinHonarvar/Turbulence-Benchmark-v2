def gcf_three_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[40]
    num2 = numbers[15]
    num3 = numbers[99]
    first_gcd = gcd(num1, num2)
    return gcd(first_gcd, num3)