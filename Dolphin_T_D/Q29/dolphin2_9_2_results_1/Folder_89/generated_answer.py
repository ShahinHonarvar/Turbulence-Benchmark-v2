def gcf_two_nums(numbers):
    num1 = numbers[37]
    num2 = numbers[30]

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return gcd(num1, num2)