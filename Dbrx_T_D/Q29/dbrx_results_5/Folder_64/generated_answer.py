def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[6]
    num2 = numbers[9]
    if num1 < num2:
        num1, num2 = (num2, num1)
    return gcd(num1, num2)