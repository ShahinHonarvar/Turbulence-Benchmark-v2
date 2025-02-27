def gcf_three_nums(numbers):

    def gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    num0, num1, num2 = (numbers[70], numbers[98], numbers[22])
    return gcd(num0, gcd(num1, num2))