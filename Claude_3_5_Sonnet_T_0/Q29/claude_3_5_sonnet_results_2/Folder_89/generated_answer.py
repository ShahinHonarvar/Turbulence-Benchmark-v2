def gcf_two_nums(numbers):

    def gcd(a, b):
        while b:
            a, b = (b, a % b)
        return a
    num1 = numbers[37]
    num2 = numbers[30]
    return gcd(num1, num2)