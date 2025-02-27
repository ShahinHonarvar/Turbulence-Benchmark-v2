def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[48]
    num2 = numbers[76]
    if num1 < 0:
        num1 = -num1
    if num2 < 0:
        num2 = -num2
    return gcd(num1, num2) if num1 <= num2 else gcd(num2, num1)