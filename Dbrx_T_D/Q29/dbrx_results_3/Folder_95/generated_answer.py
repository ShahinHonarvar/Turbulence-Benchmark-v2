def gcf_two_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num1 = numbers[43]
    num2 = numbers[99]
    if num1 < num2:
        num1, num2 = (num2, num1)
    return num1 // gcd(num1, num2)